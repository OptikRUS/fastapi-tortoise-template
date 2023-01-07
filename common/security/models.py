from enum import Enum
from pydantic import BaseModel


class Token(BaseModel):
    """
    Модель для токена
    """
    access_token: str


class UserType(str, Enum):
    """
    Модель типов пользователей
    """
    ANY = "any_user"
    ADMIN = "admin"
