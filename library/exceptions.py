from fastapi import status
from .entities import BaseLibraryException


class LibraryFullNameError(BaseLibraryException):
    message: str = "Отсутствует ФИО автора."
    status: int = status.HTTP_404_NOT_FOUND


class GenreAlreadyExistError(BaseLibraryException):
    message: str = "Такой жанр уже существует."
    status: int = status.HTTP_409_CONFLICT


class GenresNotFoundError(BaseLibraryException):
    message: str = "Жанры не найдены."
    status: int = status.HTTP_404_NOT_FOUND
