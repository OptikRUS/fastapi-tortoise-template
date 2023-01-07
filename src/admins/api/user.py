from fastapi import APIRouter, Depends, Query

from common.security import UserAuth, UserType
from src.users.repos import User
from src.users.models import UserResponse
from src.users.exceptions import BaseUserExceptionModel
from ..use_cases import GetUsersForAdmin, ApproveUserByAdmin, BlockUserByAdmin, UnblockUserByAdmin
from ..models import UserApprovedResponse, UserBlockedResponse
from ..exceptions import BaseAdminExceptionModel

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
        400: {"model": BaseAdminExceptionModel},
        404: {"model": BaseUserExceptionModel},
        409: {"model": BaseUserExceptionModel}
    }
)
async def approve_user(user_id: int, current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Подтверждение пользователя админом
    """

    approved_user: ApproveUserByAdmin = ApproveUserByAdmin(user_id=user_id, current_user=current_admin)
    return await approved_user()


@router.patch(
    "/block/{user_id}",
    response_model=UserBlockedResponse,
    responses={
        400: {"model": BaseAdminExceptionModel},
        404: {"model": BaseUserExceptionModel},
        409: {"model": BaseUserExceptionModel}
    }
)
async def block_user(user_id: int, current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Блокировка пользователя админом
    """

    blocked_user: BlockUserByAdmin = BlockUserByAdmin(user_id=user_id, current_user=current_admin)
    return await blocked_user()


@router.patch(
    "/unblock/{user_id}",
    response_model=UserBlockedResponse,
    responses={
        400: {"model": BaseAdminExceptionModel},
        404: {"model": BaseUserExceptionModel},
        409: {"model": BaseUserExceptionModel}
    }
)
async def unblock_user(user_id: int, current_admin: User = Depends(UserAuth(UserType.ADMIN))):
    """
    Разблокировка пользователя админом
    """

    unblocked_user: UnblockUserByAdmin = UnblockUserByAdmin(user_id=user_id, current_user=current_admin)
    return await unblocked_user()
