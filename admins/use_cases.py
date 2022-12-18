from typing import Optional

from users.models import User
from .schemas import UserForAdminResponse
from users.exceptions import UserNotFoundError


class GetUsersForAdmin:
    """
    Кейс получения пользователей для админа
    """

    async def __call__(self, user_id: Optional[int]):
        if user_id:
            user = await User.get_or_none(id=user_id)
            if not user:
                raise UserNotFoundError
            return UserForAdminResponse.from_orm(user)
        users = await User.all()
        return users
