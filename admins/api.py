from fastapi import APIRouter, Depends

from users.models import Users, UserForAdminResponse
from users.security import get_current_admin
from users.use_cases import GetUser
from .use_cases import GetAllUsers


admins_router = APIRouter(prefix="/admins", tags=["admins"])


@admins_router.get("/all_users", response_model=list[UserForAdminResponse])
async def get_all_users_for_admin(current_admin: Users = Depends(get_current_admin)):
    """
    Список всех пользователей для админа
    """
    all_users = GetAllUsers()
    return await all_users()


@admins_router.get("/{user_id}", response_model=UserForAdminResponse)
async def get_user_for_admin(user_id: int, current_admin: Users = Depends(get_current_admin)):
    """
    Получить информации о пользователе для админа
    """
    get_some_user = GetUser()
    return await get_some_user(user_id)
