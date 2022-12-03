from datetime import datetime

from pydantic import BaseModel, Field


class CreateAuthor(BaseModel):
    first_name: str = Field("Имя автора", min_length=2, max_length=50)
    last_name: str = Field("Фамилия автора", min_length=2, max_length=50)
    patronymic_name: str = Field("Отчество автора", min_length=2, max_length=50)
    date_of_birth = datetime
    date_of_death = datetime


class AuthorResponse(CreateAuthor):
    id: int


class CreateGenre(BaseModel):
    name: str = Field("Жанр для книги", min_length=5, max_length=25)


class GenreResponse(CreateGenre):
    id: int


class CreateBook(BaseModel):
    title: str = Field("Название книги", min_length=1, max_length=200)
    author: int
    summary: str = Field("Описание книги")
    genre: int
    updated_at: datetime
    created_at: datetime


class BookResponse(CreateBook):
    id: int
