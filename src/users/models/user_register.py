from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, Extra, SecretStr


class UserRegisterRequest(BaseModel):
    """
    Модель запроса регистрации пользователя
    """

    username: str = Field("username", min_length=3, max_length=20)
    first_name: str = Field("Имя", max_length=50)
    last_name: str = Field("Фамилия", max_length=50)
    patronymic_name: str = Field("Отчество", max_length=50)
    email: EmailStr
    phone: str = Field("+79999999999", max_length=15)
    password: str = Field("password123", max_length=128)

    # для добавления is_superuser = True в @su_registration
    class Config:
        extra = Extra.allow


class UserRegisterResponse(UserRegisterRequest):
    """
    Модель ответа регистрации пользователя
    """

    full_name_or_username: str = Field("Фамилия Имя Отчество")
    is_active: bool
    is_approved: bool
    is_superuser: bool
    updated_at: datetime
    created_at: datetime
    password: SecretStr = Field(None, exclude=True)

    class Config:
        orm_mode = True
