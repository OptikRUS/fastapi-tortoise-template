from fastapi import status
from .entities import BaseLibraryException

"""
Пример через HTTP Exception
"""


class LibraryNotFoundError(BaseLibraryException):
    status: int = status.HTTP_404_NOT_FOUND


class LibraryAlreadyExistError(BaseLibraryException):
    status: int = status.HTTP_409_CONFLICT


class LibraryFullNameError(LibraryNotFoundError):
    message: str = "Отсутствует ФИО автора."


class GenreAlreadyExistError(LibraryNotFoundError):
    message: str = "Такой жанр уже существует."


class GenresNotFoundError(LibraryNotFoundError):
    message: str = "Жанры не найдены."


class GenreNotFoundError(LibraryNotFoundError):
    message: str = "Жанр не найден."


class AuthorsNotFoundError(LibraryNotFoundError):
    message: str = "Авторы не найдены."


class AuthorNotFoundError(LibraryNotFoundError):
    message: str = "Автор не найден."


class AuthorAlreadyExistError(LibraryAlreadyExistError):
    message: str = "Такой автор уже существует."


class BooksNotFoundError(LibraryNotFoundError):
    message: str = "Книги не найдены."


class BookNotFoundError(LibraryNotFoundError):
    message: str = "Книга не найдена."


class BookAlreadyExistError(LibraryAlreadyExistError):
    message: str = "Книга с таким названием уже существует."
