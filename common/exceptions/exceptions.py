from fastapi import status

from .base import BaseHTTPException

"""
Базовые ошибки
"""


class BaseBadRequestError(BaseHTTPException):
    """
    Базовая 400 ошибка
    """
    status: int = status.HTTP_400_BAD_REQUEST


class BaseNotAuthError(BaseHTTPException):
    """
    Базовая 401 ошибка
    """
    status: int = status.HTTP_401_UNAUTHORIZED


class BaseForbiddenError(BaseHTTPException):
    """
    Базовая 403 ошибка
    """
    status: int = status.HTTP_403_FORBIDDEN


class BaseNotFoundError(BaseHTTPException):
    """
    Базовая 404 ошибка
    """
    status: int = status.HTTP_404_NOT_FOUND


class BaseConflictError(BaseHTTPException):
    """
    Базовая 409 ошибка
    """
    status: int = status.HTTP_409_CONFLICT
