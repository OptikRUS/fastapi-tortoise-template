import time

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from src.users import exceptions as exc
from src.users.repos import User
from .models import Token, UserType

from config import auth_config

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl=auth_config.get('token_url'))
hasher: CryptContext = CryptContext(
    schemes=auth_config.get("hasher_schemes"),
    deprecated=auth_config.get("hasher_deprecated")
)


class UserLogin:
    """
    Кейс получения токена
    """
    secret_key: str = auth_config.get("secret_key")
    algorithm: str = auth_config.get("algorithm")
    expires: int = auth_config.get("expires")

    def __init__(self, username: str, password: str) -> None:
        self.username, self.password = username, password
        self.password_hash: CryptContext = hasher

    async def __call__(self) -> Token:
        user: User = await self.authenticate_user()
        if user:
            access_token: str = self.sign_jwt()
            return Token(access_token=access_token)
        raise exc.UserWrongPasswordError

    async def authenticate_user(self) -> User | bool:
        """
        Аутентификация пользователя
        """
        user = await User.get_or_none(username=self.username)
        if not user:
            return False
        if not self.verify_password(self.password, user.password):
            return False
        return user

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Проверка пароля
        """
        return self.password_hash.verify(plain_password, hashed_password)

    def sign_jwt(self) -> str:
        """
        Генерация токена
        """
        payload = {
            "username": self.username,
            "expires": time.time() + self.expires
        }
        token = jwt.encode(
            payload=payload,
            key=self.secret_key,
            algorithm=self.algorithm
        )
        return token


class UserAuth:
    """
    Класс авторизации пользователя
    """
    secret_key: str = auth_config.get("secret_key")
    algorithm: str = auth_config.get("algorithm")

    def __init__(self, user_type: UserType) -> None:
        self.user_type = user_type

    async def __call__(self, token: str = Depends(oauth2_scheme)) -> User:
        token_dict = self.decode_jwt(token)
        if not token_dict:
            raise exc.UserTokenTimeOutError

        user = await User.get_or_none(username=token_dict.get('username'))
        if not user:
            raise exc.UserNotAuthError

        if not user.is_active:
            raise exc.UserNotActiveError

        if self.user_type == UserType.ADMIN and not user.is_superuser:
            raise exc.UserForbiddenError
        return user

    def decode_jwt(self, token: str) -> dict:
        """
        Проверка токена
        """
        try:
            decoded_token = jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=self.algorithm,
            )
            if decoded_token.get("expires") >= time.time():
                return decoded_token
        except Exception as e:
            return {"error": e}
