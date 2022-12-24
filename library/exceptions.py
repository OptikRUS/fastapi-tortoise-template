from fastapi import status
from .entities import BaseLibraryException

"""
Пример через HTTP Exception
"""


class LibraryNotFoundError(BaseLibraryException):
    status: int = status.HTTP_404_NOT_FOUND


class LibraryAlreadyExistError(BaseLibraryException):
    status: int = status.HTTP_409_CONFLICT
    reason: str = "already_exist_error"


class AuthorFullNameError(LibraryNotFoundError):
    message: str = "Отсутствует ФИО автора."
    status: int = status.HTTP_400_BAD_REQUEST
    reason: str = "author_full_name_error"


class GenreAlreadyExistError(LibraryAlreadyExistError):
    message: str = "Такой жанр уже существует."
    reason: str = "genre_already_exist"


class GenresNotFoundError(LibraryNotFoundError):
    message: str = "Жанры не найдены."
    reason: str = "genres_not_found"


class GenreNotFoundError(LibraryNotFoundError):
    message: str = "Жанр не найден."
    reason: str = "genre_not_found"


class AuthorsNotFoundError(LibraryNotFoundError):
    message: str = "Авторы не найдены."
    reason: str = "authors_not_found"


class AuthorNotFoundError(LibraryNotFoundError):
    message: str = "Автор не найден."
    reason: str = "author_not_found"


class AuthorAlreadyExistError(LibraryAlreadyExistError):
    message: str = "Такой автор уже существует."
    reason: str = "author_already_exist"


class BooksNotFoundError(LibraryNotFoundError):
    message: str = "Книги не найдены."
    reason: str = "books_not_found"


class BookNotFoundError(LibraryNotFoundError):
    message: str = "Книга не найдена."
    reason: str = "book_not_found"


class BookAlreadyExistError(LibraryAlreadyExistError):
    message: str = "Книга с таким названием уже существует."
    reason: str = "book_already_exist"
