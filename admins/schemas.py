from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserForAdminResponse(BaseModel):
    id: int
    username: str = Field("username", min_length=6, max_length=20)
    first_name: str = Field("Имя", max_length=50)
    last_name: str = Field("Фамилия", max_length=50)
    patronymic_name: str = Field("Отчество", max_length=50)
    email: EmailStr
    phone: str = Field("+79999999999", max_length=15)
    is_active: bool
    is_approved: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
