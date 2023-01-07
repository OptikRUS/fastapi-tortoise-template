from src.users.models import UserRegisterRequest


def su_registration(superusers: list):
    """
    Регистрация суперпользователей
    """
    def registration(method):
        async def _wrapper(init, user: UserRegisterRequest):
            if user.username in superusers:
                user.is_superuser = True
                return await method(init, user)
            return await method(init, user)
        return _wrapper
    return registration
