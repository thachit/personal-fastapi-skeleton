from fastapi import APIRouter
from typing import List
from src.api.schemas.users import UserResponse
from src.services.users import get_all_users
user_router_v2 = APIRouter(
    prefix="/users",
    tags=["users"],
)

@user_router_v2.get("/", response_model=List[UserResponse])
async def read_users():
    response = await get_all_users()
    return response
