from datetime import datetime, timezone
from fastapi import FastAPI, Response, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse
from src.utils.log import setup_logging
from src.core.config import Config
from src.api.api_v1.users import user_router_v1
from src.api.api_v2.users import user_router_v2
from src.db.db import db_check

setup_logging()

fast_api = FastAPI()

fast_api.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS.split(",") if Config.ALLOWED_ORIGINS else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@fast_api.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors_string = ""
    for error in exc.errors():
        loc = error.get('loc', ())
        field_name = loc[1] if len(loc) > 1 else ""
        error_ctx = error.get('ctx')
        errors_string = errors_string + \
                        f"{field_name} {error.get('msg', '')}, "

    return JSONResponse(content=jsonable_encoder({"detail": errors_string.strip()}),
                        status_code=status.HTTP_400_BAD_REQUEST)

# API V1
fast_api.include_router(user_router_v1, prefix='/api/v1')

# API V2
fast_api.include_router(user_router_v2, prefix='/api/v2')


@fast_api.get("/health")
async def health_check(response: Response):
    db_status = db_check()
    if db_status is True:
        return {
            "status": "ok",
            "timestamp": datetime.now(timezone.utc).isoformat() + "Z",
            "app_name": Config.APP_NAME,
            "app_environment": Config.APP_ENV,
            "version": Config.APP_VERSION,
            "dependencies": {
                "database": "ok"
            }
        }
    else:
        response.status_code = 503
        return {
          "status": "degraded",
          "dependencies": {
            "database": "fail" if db_status is False else "ok"
          }
        }