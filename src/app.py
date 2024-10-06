from fastapi import FastAPI
from src.core.config import Config
from src.api.api_v1.users import user_router_v1
from src.api.api_v2.users import user_router_v2

fast_api = FastAPI()

# API V1
fast_api.include_router(user_router_v1, prefix='/api/v1')

# API V2
fast_api.include_router(user_router_v2, prefix='/api/v2')


@fast_api.get("/health")
async def health_check():
    return {
        "status": "ok",
        "app_name": Config.APP_NAME
    }