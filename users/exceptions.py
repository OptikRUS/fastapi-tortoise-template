from fastapi import status
from .entities import BaseUserException

"""
Пример через Base Exception
"""


class UserTokenTimeOutError(BaseUserException):
    message: str = "Время кода истекло."
    status: int = status.HTTP_401_UNAUTHORIZED
    reason: str = "user_token_timeout"


class UserWrongPasswordError(BaseUserException):
    message: str = "Введён неверный пароль."
    status: int = status.HTTP_401_UNAUTHORIZED
    reason: str = "user_wrong_password"


class UserAlreadyRegisteredError(BaseUserException):
    message: str = "Пользователь с таким ником уже зарегистрирован."
    status: int = status.HTTP_409_CONFLICT
    reason: str = "user_already_exist"


class UserEmailTakenError(UserAlreadyRegisteredError):
    message: str = "Введенный email занят."
    reason: str = "user_mail_already_exist"


class UserPhoneTakenError(UserAlreadyRegisteredError):
    message: str = "Введённый номер телефона занят."
    reason: str = "user_phone_already_exist"


class UserNotAuthError(UserWrongPasswordError):
    message: str = "Пользователь не авторизован."
    reason: str = "user_not_auth"


class UserNotActiveErrorHTTP(BaseUserException):
    message: str = "Пользователь неактивен."
    status: int = status.HTTP_403_FORBIDDEN
    reason: str = "user_not_active"


class UserForbiddenError(BaseUserException):
    message: str = "У пользователя нет прав."
    status: int = status.HTTP_403_FORBIDDEN
    reason: str = "user_have_not_permissions"
    headers: dict = {"WWW-Authenticate": "Bearer"}


class UserNotFoundError(BaseUserException):
    message: str = "Пользователь не найден."
    status: int = status.HTTP_404_NOT_FOUND
    reason: str = "user_not_found"
