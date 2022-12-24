from .schemas import UserRegister
from .models import User, UserResponse, UserUpdate
from .exceptions import UserAlreadyRegisteredError, UserEmailTakenError, UserPhoneTakenError, UserNotFoundError
from .maintenance import su_registration
from common.security import hasher

from config import super_users_config


class UserRegistration:
    """
    Кейс регистрации пользователя
    """

    def __init__(self) -> None:
        self.hasher = hasher

    @su_registration(super_users_config.get("superusers"))
    async def __call__(self, user: UserRegister) -> UserResponse:

        username = await User.get_or_none(username=user.username)
        if username:
            raise UserAlreadyRegisteredError

        user_email = await User.get_or_none(email=user.email)
        if user_email:
            raise UserEmailTakenError

        user_phone = await User.get_or_none(phone=user.phone)
        if user_phone:
            raise UserPhoneTakenError

        user.password = self.hasher.hash(user.password)
        new_user = await User.create(**user.dict(exclude_unset=True))
        return await UserResponse.from_tortoise_orm(new_user)


class GetUser:
    """
    Кейс получения пользователя
    """

    async def __call__(self, user_id: int):
        user = await User.get_or_none(id=user_id)
        if user:
            return user
        raise UserNotFoundError


class UpdateUserProfile:
    """
    Кейс изменения информации пользователя
    """

    def __init__(self, current_user: User) -> None:
        self.current_user = current_user

    async def __call__(self, user_data: dict) -> UserUpdate:
        updated_user = await self.current_user.update_from_dict(user_data)
        await updated_user.save()
        return updated_user
