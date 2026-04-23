from sqlalchemy import Boolean, Column, String, DateTime
from src.models.base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    email = Column(String, unique=True, index=False)
    phone_number = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, nullable=False, default=True)
    last_login = Column(DateTime(timezone=True), nullable=True)