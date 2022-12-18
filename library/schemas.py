from datetime import date, datetime

from pydantic import BaseModel, Field, validator


class CreateAuthor(BaseModel):
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


class AuthorResponse(CreateAuthor):
    id: int
    full_name: str

    class Config:
        orm_mode = True


class CreateGenre(BaseModel):
    name: str = Field("Жанр для книги", min_length=4, max_length=25)


class GenreResponse(CreateGenre):
    id: int

    class Config:
        orm_mode = True


class CreateBook(BaseModel):
    title: str = Field("Название книги", min_length=1, max_length=200)
    author_id: int
    genres_id: list[int]
    summary: str = Field("Описание книги")


class BookResponse(BaseModel):
    id: int
    title: str
    summary: str
    author: AuthorResponse
    genres: list[GenreResponse]
    updated_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True


class BooksResponse(BaseModel):
    count: int
    found_books: list[BookResponse]
