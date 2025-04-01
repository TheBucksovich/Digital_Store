from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: int
    is_active: bool
