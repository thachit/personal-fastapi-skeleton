import os
from pydantic import BaseSettings

class Config:
    APP_NAME = os.getenv("APP_NAME", "My Fast API app 1")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "nguyencothach1989@gmail.com")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", 1)
