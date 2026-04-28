from pydantic import BaseModel, ConfigDict
from uuid import UUID

class UserBase(BaseModel):
    is_active: bool
    email: str


class UserResponse(UserBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)