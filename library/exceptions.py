from fastapi import status
from .entities import BaseAuthorException


class AuthorFullNameError(BaseAuthorException):
    message: str = "Отсутствует ФИО автора."
    status: int = status.HTTP_404_NOT_FOUND
