from .base import UserUpdateResponse


class UserApprovedResponse(UserUpdateResponse):
    is_approved: bool


class UserBlockedResponse(UserUpdateResponse):
    is_active: bool
