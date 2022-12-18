from users.models import User, UserForAdminResponse


class GetAllUsers:
    """
    Кейс получения всех пользователей для админа
    """

    async def __call__(self):
        all_users = await UserForAdminResponse.from_queryset(User.all())
        if all_users:
            return all_users
