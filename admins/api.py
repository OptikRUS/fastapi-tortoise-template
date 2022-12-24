from fastapi import APIRouter, Depends, Query

from users.models import User
from common.security import UserAuth, UserType
from .schemas import UserForAdminResponse
from .use_cases import GetUsersForAdmin


admins_router = APIRouter(prefix="/admins", tags=["admins"])


@admins_router.get("/users", response_model=list[UserForAdminResponse])
async def get_users_for_admin(user_id: int = Query(None), current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Получение пользователей для админа
    """

    users = GetUsersForAdmin()
    return await users(user_id=user_id)
