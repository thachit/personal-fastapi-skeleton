import os
from pydantic import BaseSettings

class Config:
    APP_NAME = os.getenv("APP_NAME", "My Fast API app")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "nguyencothach1989@gmail.com")
    DATABASE_DRIVER = os.getenv("DATABASE_DRIVER", "postgresql+psycopg2")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = os.getenv("DATABASE_PORT", "5432")
    DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", None)
    DATABASE_NAME = os.getenv("DATABASE_NAME", "postgres")
    DEBUG = os.getenv("DEBUG", "false").lower() in ("true", 1)
