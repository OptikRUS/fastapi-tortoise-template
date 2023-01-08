from datetime import datetime

from pydantic import Field

from ..entities import BaseBookModel
from .author import AuthorResponse
from .genre import GenreResponse


class BaseBook(BaseBookModel):
    """
    Модель книги
    """

    title: str = Field("Название книги", min_length=1, max_length=200)
    summary: str = Field("Описание книги")


class CreateBookRequest(BaseBook):
    """
    Модель запроса создания книги
    """

    author_id: int
    genres_id: list[int]


class BookResponse(BaseBook):
    """
    Модель ответа для книги
    """

    updated_at: datetime
    created_at: datetime


class BookDetailResponse(BookResponse):
    """
    Модель ответа информации для книги
    """

    id: int
    author: AuthorResponse
    genres: list[GenreResponse] | GenreResponse

    class Config:
        orm_mode = True


class BooksResponse(BaseBookModel):
    """
    Модель ответа информации для книг
    """

    count: int
    found_books: list[BookResponse]
