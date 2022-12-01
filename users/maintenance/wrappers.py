from ..models import Users, UserResponse
from ..schemas import UserRegister


def su_registration(superusers: list):
    """
    Регистрация суперпользователей
    """
    def registration(method):
        async def _wrapper(init, user: UserRegister) -> UserResponse:
            if user.username in superusers:
                user.is_superuser = True
                return await method(init, user)
            return await method(init, user)
        return _wrapper
    return registration
