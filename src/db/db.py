from src.utils.log import get_logger
from contextlib import contextmanager
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import text
from src.core.config import Config

logger = get_logger(__name__)

database = URL.create(
    drivername=Config.DATABASE_DRIVER,
    host=Config.DATABASE_HOST,
    port=Config.DATABASE_PORT,
    database=Config.DATABASE_NAME,
    username=Config.DATABASE_USER,
    password=Config.DATABASE_PASSWORD
)

engine = create_engine(database, echo=True if Config.DEBUG else False, pool_pre_ping=True)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass


@contextmanager
def get_session():
    session = session_local()
    try:
        yield session
    finally:
        session.close()

@contextmanager
def get_transaction_session():
    session = session_local()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error(f"Transaction error: {e}")
        raise e
    finally:
        session.close()


def db_check():
    try:
        with get_session() as session:
            session.execute(text("SELECT 1"))
            return True
    except Exception as e:
        logger.error(f"---------- db_check error: {e}")
        return False
