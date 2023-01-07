from datetime import date

from pydantic import Field, validator

from ..entities import BaseAuthorModel


class CreateAuthorRequest(BaseAuthorModel):
    """
    Модель запроса создания автора
    """

    first_name: str = Field("Имя автора", min_length=2, max_length=50)
    last_name: str = Field("Фамилия автора", min_length=2, max_length=50)
    patronymic_name: str | None = Field("Отчество автора", max_length=50)
    date_of_birth: date
    date_of_death: date

    @validator("date_of_birth", allow_reuse=True)
    def check_date_of_birth(cls, date_of_birth):
        if date_of_birth > date.today():
            raise ValueError("Некорректная дата рождения")
        return date_of_birth

    @validator("date_of_death", allow_reuse=True)
    def check_date_of_death(cls, date_of_death):
        if date_of_death > date.today():
            raise ValueError("Некорректная дата смерти")
        return date_of_death


class AuthorResponse(CreateAuthorRequest):
    """
    Модель ответа для автора
    """

    id: int
    full_name: str

    class Config:
        orm_mode = True
