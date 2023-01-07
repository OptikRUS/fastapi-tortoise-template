from src.users.repos import User
from src.users.exceptions import UserAlreadyBlockedError
from .base_patch import BasePatch


class BlockUserByAdmin(BasePatch):
    """
    Кейс блокировки пользователя админом
    """

    async def __call__(self):
        user = await self.get_user()
        if not user.is_active:
            raise UserAlreadyBlockedError

        blocked_user_data: dict = dict(is_active=False)
        blocked_user: User = await self.user_repo.update(user, data=blocked_user_data)
        return blocked_user
