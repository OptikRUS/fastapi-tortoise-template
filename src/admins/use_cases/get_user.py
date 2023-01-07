from typing import Optional

from src.users.repos import UserRepo, User
from src.users.exceptions import UserNotFoundError


class GetUsersForAdmin:
    """
    Кейс получения пользователей для админа
    """

    def __init__(self) -> None:
        self.user_repo: UserRepo = UserRepo()

    async def __call__(self, user_id: Optional[int]):
        filters: dict = dict()

        if user_id:
            filters = dict(id=user_id)

        users: list[User] = await self.user_repo.list(filters=filters)
        if users:
            return users
        raise UserNotFoundError
