import time

import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


from .schemas import Token
from ..models import Users as DB_User
from ..exceptions import UserNotAuthError, UserForbiddenError, UserNotActiveError, UserTokenTimeoutError

from config import auth_config

oauth2_scheme: OAuth2PasswordBearer = OAuth2PasswordBearer(tokenUrl=auth_config.get('token_url'))


def get_hasher() -> CryptContext:
    """
    Получение хэшера
    """
    hasher: CryptContext = CryptContext(
        schemes=auth_config["hasher_schemes"], deprecated=auth_config["hasher_deprecated"]
    )
    return hasher


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Проверка пароля
    """
    password_hash = get_hasher()
    return password_hash.verify(plain_password, hashed_password)


async def authenticate_user(username: str, password: str) -> DB_User | bool:
    """
    Аутентификация пользователя
    """
    user = await DB_User.get_or_none(username=username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def sign_jwt(username: str) -> Token:
    """
    Генерация токена
    """
    payload = {
        "username": username,
        "expires": time.time() + auth_config["expires"]
    }
    token = jwt.encode(
        payload=payload,
        key=auth_config["secret_key"],
        algorithm=auth_config["algorithm"]
    )
    return Token(access_token=token)


def decode_jwt(token: str) -> dict:
    """
    Проверка токена
    """
    try:
        decoded_token = jwt.decode(
            jwt=token,
            key=auth_config["secret_key"],
            algorithms=auth_config["algorithm"],
        )
        if decoded_token["expires"] >= time.time():
            return decoded_token
        raise UserTokenTimeoutError
    except Exception as e:
        return {"error": e}


async def get_current_user(token: str = Depends(oauth2_scheme)) -> DB_User:
    """
    Проверка авторизации пользователя
    """
    token_dict = decode_jwt(token)
    if not token_dict:
        raise UserNotAuthError
    user = await DB_User.get_or_none(username=token_dict['username'])
    if user is None:
        raise UserNotAuthError
    return user


async def get_current_admin(token: str = Depends(oauth2_scheme)) -> DB_User:
    """
    Проверка авторизации админа
    """

    token_dict = decode_jwt(token)
    if not token_dict:
        raise UserNotAuthError
    user = await DB_User.get_or_none(username=token_dict['username'])
    if not user.is_superuser:
        raise UserForbiddenError
    return user


async def get_current_active_user(current_user: DB_User = Depends(get_current_user)) -> DB_User:
    """
    Проверка авторизации и активности пользователя
    """
    if not current_user.is_active:
        raise UserNotActiveError
    return current_user
