from .base import UserUpdateResponse


class UserApprovedResponse(UserUpdateResponse):
    """
    Модель подтверждения пользователя
    """
    is_approved: bool


class UserBlockedResponse(UserUpdateResponse):
    """
    Модель блокировки/разблокировки пользователя
    """
    is_active: bool
