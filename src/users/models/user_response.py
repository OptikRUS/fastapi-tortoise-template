from .user_register import UserRegisterResponse


class UserResponse(UserRegisterResponse):
    """
    Модель ответа пользователя
    """
    id: int
