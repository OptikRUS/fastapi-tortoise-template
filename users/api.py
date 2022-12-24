from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from tortoise.contrib.fastapi import HTTPNotFoundError

from common.security import UserAuth, UserLogin, Token, UserType
from .models import User, UserResponse, UserUpdate
from .schemas import UserRegister
from .use_cases import UserRegistration, GetUser, UpdateUserProfile

users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.post("/register", status_code=201, response_model=UserResponse)
async def register_user(user: UserRegister):
    """
    Регистрация пользователя
    """
    user_register = UserRegistration()
    return await user_register(user)


@users_router.post("/login", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Авторизация пользователя
    """
    access_token = UserLogin(form_data.username, form_data.password)
    return await access_token()


@users_router.get("/me", status_code=200, response_model=UserResponse)
async def get_me(current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Получить информацию о себе
    """
    return current_user


@users_router.get(
    "/{user_id}", response_model=UserResponse, responses={404: {"model": HTTPNotFoundError}}
)
async def get_user(user_id: int):
    """
    Получить информации о пользователе
    """
    get_some_user = GetUser()
    return await get_some_user(user_id)


@users_router.put(
    "/update_me", response_model=UserUpdate, responses={404: {"model": HTTPNotFoundError}}
)
async def update_me(user: UserUpdate, current_user: User = Depends(UserAuth(UserType.ANY))):
    """
    Изменение информации пользователя
    """
    user_update = UpdateUserProfile(current_user)
    return await user_update(user.dict())


# @users_router.delete("/user/{user_id}", response_model=Status, responses={404: {"model": HTTPNotFoundError}})
# async def delete_user(user_id: int):
#     deleted_count = await Users.filter(id=user_id).delete()
#     if not deleted_count:
#         raise HTTPException(status_code=404, detail=f"User {user_id} not found")
#     return Status(message=f"Deleted user {user_id}")
