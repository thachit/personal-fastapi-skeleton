from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str


class UserResponse(UserBase):
    id: int