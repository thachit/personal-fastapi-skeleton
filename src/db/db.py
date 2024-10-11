from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.core.config import Config

database = URL.create(
    drivername=Config.DATABASE_DRIVER,
    host=Config.DATABASE_HOST,
    port=Config.DATABASE_PORT,
    database=Config.DATABASE_NAME,
    username=Config.DATABASE_USER,
    password=Config.DATABASE_PASSWORD
)

engine = create_engine(database, echo=True if Config.DEBUG else False)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
