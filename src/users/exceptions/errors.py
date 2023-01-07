from common.exceptions import BaseNotAuthError, BaseForbiddenError, BaseNotFoundError, BaseConflictError

"""
Ошибки пользователя
"""


class UserTokenTimeOutError(BaseNotAuthError):
    message: str = "Время кода истекло."
    reason: str = "user_token_timeout"


class UserWrongPasswordError(BaseNotAuthError):
    message: str = "Введён неверный пароль."
    reason: str = "user_wrong_password"


class UserNotActiveError(BaseForbiddenError):
    message: str = "Пользователь неактивен."
    reason: str = 'user_not_active'
    headers: dict = {"WWW-Authenticate": "Bearer"}


class UserForbiddenError(BaseForbiddenError):
    message: str = "У пользователя нет прав."
    reason: str = 'user_forbidden_error'


class UserNotFoundError(BaseNotFoundError):
    message: str = "Пользователь не найден."
    reason: str = "user_not_found"


class UsersNotFoundError(BaseNotFoundError):
    message: str = "Пользователи не найдены."
    reason: str = "users_not_found"


class UserAlreadyRegisteredError(BaseConflictError):
    message: str = "Пользователь с таким ником уже зарегистрирован."
    reason: str = "username_already_exist"


class UserEmailTakenError(BaseConflictError):
    message: str = "Введенный email занят."
    reason: str = "user_email_already_exist"


class UserPhoneTakenError(BaseConflictError):
    message: str = "Введённый номер телефона занят."
    reason: str = "user_phone_already_exist"


class UserNotAuthError(BaseConflictError):
    message: str = "Пользователь не авторизован."
    reason: str = "user_not_auth"


class UserAlreadyApprovedError(BaseConflictError):
    message: str = "Пользователь уже подтверждён."
    reason: str = "user_already_approved"


class UserAlreadyBlockedError(BaseConflictError):
    message: str = "Пользователь уже заблокирован."
    reason: str = "user_already_blocked"


class UserAlreadyUnblockedError(BaseConflictError):
    message: str = "Пользователь уже разблокирован."
    reason: str = "user_already_unblocked"
