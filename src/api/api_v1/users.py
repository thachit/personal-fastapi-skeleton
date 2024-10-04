from fastapi import APIRouter, Depends
from src.api.schemas.users import UserResponse
user_router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@user_router.get("/", response_model=UserResponse)
async def read_users():
    import os
    cwd = os.getcwd()
    return {
        "id": 1,
        "username": f"thachit: {str(cwd)}",
        "email": "nguyencothach1989@gmail.com",
    }
