from fastapi import APIRouter
from typing import List
from src.schemas.users import UserResponse
from src.services.users import get_all_users
user_router_v1 = APIRouter(
    prefix="/users",
    tags=["users"],
)

@user_router_v1.get("/", response_model=List[UserResponse])
async def read_users():
    response = await get_all_users()
    return response
