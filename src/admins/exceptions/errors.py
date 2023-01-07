from common.exceptions import BaseBadRequestError

"""
Ошибки админки
"""


class AdminSelfMatchError(BaseBadRequestError):
    message: str = "Недоступно для себя."
    reason: str = "self_match_error"
