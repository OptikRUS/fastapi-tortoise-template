from src.users.repos import UserRepo, User
from src.users.exceptions import UserNotFoundError, UserAlreadyApprovedError


class ApproveUserByAdmin:
    """
    Кейс подтверждения пользователя админом
    """

    def __init__(self) -> None:
        self.user_repo: UserRepo = UserRepo()

    async def __call__(self, user_id: int):
        filters: dict = dict(id=user_id)

        user: User = await self.user_repo.retrieve(filters=filters)
        if not user:
            raise UserNotFoundError

        if user.is_approved:
            raise UserAlreadyApprovedError

        approval_data: dict = dict(is_approved=True)
        approved_user: User = await self.user_repo.update(user, data=approval_data)
        return approved_user
