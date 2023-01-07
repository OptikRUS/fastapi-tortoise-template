from pydantic import BaseModel, EmailStr, Field


class UserUpdateRequest(BaseModel):
    """
    Модель запроса изменения пользователя
    """

    username: str = Field("username", min_length=3, max_length=20)
    first_name: str = Field("Имя", max_length=50)
    last_name: str = Field("Фамилия", max_length=50)
    patronymic_name: str = Field("Отчество", max_length=50)
    email: EmailStr
    phone: str = Field("+79999999999", max_length=15)
