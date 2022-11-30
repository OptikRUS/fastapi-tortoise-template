from users.models import Users, UserForAdminResponse


class GetAllUsers:
    """
    Кейс получения всех пользователей для админа
    """

    async def __call__(self):
        all_users = await UserForAdminResponse.from_queryset(Users.all())
        if all_users:
            return all_users
