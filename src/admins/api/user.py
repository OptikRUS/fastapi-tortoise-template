from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.users.repos import User
from src.users.models import UserResponse
from src.users.exceptions import BaseUserExceptionModel
from ..use_cases import GetUsersForAdmin, ApproveUserByAdmin
from ..models import UserApprovedResponse

router = APIRouter(prefix="/admins", tags=["admins"])


@router.get(
    "/users",
    response_model=list[UserResponse],
    responses={
        404: {"model": BaseUserExceptionModel}
    }
)
async def get_users_for_admin(user_id: int = Query(None), auth: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Получение пользователей для админа
    """

    users: GetUsersForAdmin = GetUsersForAdmin()
    return await users(user_id=user_id)


@router.patch(
    "/approve/{user_id}",
    response_model=UserApprovedResponse,
    responses={
        404: {"model": BaseUserExceptionModel},
        409: {"model": BaseUserExceptionModel}
    }
)
async def approve_user(user_id: int = Query(None), auth: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Подтверждение пользователя админом
    """

    user: ApproveUserByAdmin = ApproveUserByAdmin()
    return await user(user_id=user_id)
