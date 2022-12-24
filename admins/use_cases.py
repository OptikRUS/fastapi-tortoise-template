from typing import Optional

from users.models import User
from users.exceptions import UserNotFoundError


class GetUsersForAdmin:
    """
    Кейс получения пользователей для админа
    """

    async def __call__(self, user_id: Optional[int]):
        if user_id:
            user = await User.filter(id=user_id)
            if not user:
                raise UserNotFoundError
            return user
        users = await User.all()
        return users
