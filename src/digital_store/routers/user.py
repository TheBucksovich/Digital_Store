from http.client import HTTPException

from fastapi import APIRouter, status

from src.digital_store.schemas.user import UserResponse, UserCreate

router = APIRouter(
    tags=["users"],
)

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    """
    Создание нового пользователя (пока без БД).
    """
    new_user = {
        "id": 1, # временно
        "username": user_data.username,
        "email": user_data.email,
        "age": user_data.age,
        "is_active": True,
    }
    return new_user

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    """
    Получение пользователя по ID (временно)
    """
    if user_id == 1:
        return {
            "id": 1,
            "username": "Ilya",
            "email": "ilya@example.com",
            "age": 25,
            "is_active": True
        }
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND)