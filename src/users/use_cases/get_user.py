from ..repos import UserRepo, User
from ..exceptions import UserNotFoundError


class GetUser:
    """
    Кейс получения пользователя
    """

    def __init__(self) -> None:
        self.user_repo: UserRepo = UserRepo()

    async def __call__(self, user_id: int) -> User:
        filters: dict = dict(id=user_id)
        user: User = await self.user_repo.retrieve(filters=filters)
        if user:
            return user
        raise UserNotFoundError
