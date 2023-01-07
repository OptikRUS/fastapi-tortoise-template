from src.users.repos import UserRepo, User
from src.users.exceptions import UserNotFoundError
from ..exceptions import AdminSelfMatchError


class BasePatch:
    """
    Базовый кейс для изменения пользователя
    """

    def __init__(self, user_id: int, current_user: User) -> None:
        self.user_repo: UserRepo = UserRepo()
        self.user_id: int = user_id
        self.current_user: User = current_user

    async def get_user(self):
        if self.user_id == self.current_user.id:
            raise AdminSelfMatchError

        filters: dict = dict(id=self.user_id)
        user: User = await self.user_repo.retrieve(filters=filters)
        if not user:
            raise UserNotFoundError
        return user
