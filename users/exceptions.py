from fastapi import status
from .entities import BaseUserException


class UserWrongPasswordError(BaseUserException):
    message: str = "Введён неверный пароль."
    status: int = status.HTTP_401_UNAUTHORIZED
    headers: dict = {"WWW-Authenticate": "Bearer"}


class UserAlreadyRegisteredError(BaseUserException):
    message: str = "Пользователь с таким ником уже зарегистрирован."
    status: int = status.HTTP_400_BAD_REQUEST


class UserEmailTakenError(UserAlreadyRegisteredError):
    message: str = "Введенный email занят."


class UserPhoneTakenError(UserAlreadyRegisteredError):
    message: str = "Введённый номер телефона занят."


class UserNotAuthError(UserWrongPasswordError):
    message: str = "Пользователь не авторизован."


class UserNotActiveError(BaseUserException):
    message: str = "Пользователь неактивен."
    status: int = status.HTTP_400_BAD_REQUEST


class UserTokenTimeoutError(BaseUserException):
    message: str = "Время токена истекло."
    status: int = status.HTTP_400_BAD_REQUEST


class UserForbiddenError(BaseUserException):
    message: str = "У пользователя нет прав."
    status: int = status.HTTP_403_FORBIDDEN
    headers: dict = {"WWW-Authenticate": "Bearer"}


class UserNotFoundError(BaseUserException):
    message: str = "Пользователь не найден."
    status: int = status.HTTP_404_NOT_FOUND
