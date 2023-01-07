from ..repos import User, UserRepo
from ..models import UserUpdateRequest


class UpdateUserProfile:
    """
    Кейс изменения информации пользователя
    """

    def __init__(self, current_user: User) -> None:
        self.current_user = current_user
        self.user_repo: UserRepo = UserRepo()

    async def __call__(self, user_data: UserUpdateRequest) -> User:
        updated_user: User = await self.user_repo.update(model=self.current_user, data=user_data.dict())
        return updated_user
