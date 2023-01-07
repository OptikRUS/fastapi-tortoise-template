from src.users.repos import User
from src.users.exceptions import UserAlreadyUnblockedError
from .base_patch import BasePatch


class UnblockUserByAdmin(BasePatch):
    """
    Кейс разблокировки пользователя админом
    """

    async def __call__(self):
        user = await self.get_user()
        if user.is_active:
            raise UserAlreadyUnblockedError

        blocked_user_data: dict = dict(is_active=True)
        blocked_user: User = await self.user_repo.update(user, data=blocked_user_data)
        return blocked_user
