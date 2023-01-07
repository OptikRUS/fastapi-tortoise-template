from src.users.repos import User
from src.users.exceptions import UserAlreadyApprovedError
from .base_patch import BasePatch


class ApproveUserByAdmin(BasePatch):
    """
    Кейс подтверждения пользователя админом
    """

    async def __call__(self):
        user = await self.get_user()
        if user.is_approved:
            raise UserAlreadyApprovedError

        approval_data: dict = dict(is_approved=True)
        approved_user: User = await self.user_repo.update(user, data=approval_data)
        return approved_user
