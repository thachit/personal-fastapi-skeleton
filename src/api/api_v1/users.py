from fastapi import APIRouter
from typing import List
from src.api.schemas.users import UserResponse
from src.services.users import get_users
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@user_router.get("/", response_model=List[UserResponse])
async def read_users():
    response = await get_users()
    return response
