from fastapi import FastAPI
from src.core.config import Config
from src.api.api_v1.users import user_router
import os
cwd = os.getcwd()
print(cwd)

fast_api = FastAPI()
fast_api.include_router(user_router)

@fast_api.get("/health")
async def health_check():
    return {
        "status": "ok",
        "app_name": Config.APP_NAME
    }