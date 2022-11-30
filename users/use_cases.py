from .models import Users, UserResponse, UserUpdate
from .security.schemas import Token
from .security import authenticate_user, sign_jwt, get_hasher
from .exceptions import (UserWrongPasswordError, UserAlreadyRegisteredError, UserEmailTakenError,
                         UserPhoneTakenError, UserNotFoundError)


class UserAuth:
    """
    Кейс получения токена
    """

    async def __call__(self, username: str, password: str) -> Token:
        user: Users = await authenticate_user(username=username, password=password)
        if user:
            access_token: Token = sign_jwt(username=username)
            return access_token
        raise UserWrongPasswordError


class UserRegistration:
    """
    Кейс регистрации пользователя
    """

    def __init__(self) -> None:
        self.hasher = get_hasher()

    async def __call__(self, user: UserResponse) -> UserResponse:

        username = await Users.get_or_none(username=user.username)
        if username:
            raise UserAlreadyRegisteredError
        user_email = await Users.get_or_none(email=user.email)
        if user_email:
            raise UserEmailTakenError

        user_phone = await Users.get_or_none(phone=user.phone)
        if user_phone:
            raise UserPhoneTakenError

        user.password = self.hasher.hash(user.password)
        new_user = await Users.create(**user.dict(exclude_unset=True))
        return await UserResponse.from_tortoise_orm(new_user)


class GetUser:
    """
    Кейс получения пользователя
    """

    async def __call__(self, user_id: int):
        user = await Users.get_or_none(id=user_id)
        if user:
            return user
        raise UserNotFoundError


class UpdateUserProfile:
    """
    Кейс изменения информации пользователя
    """

    def __init__(self, current_user: Users) -> None:
        self.current_user = current_user

    async def __call__(self, user_data: dict) -> UserUpdate:
        updated_user = await self.current_user.update_from_dict(user_data)
        await updated_user.save()
        return updated_user
