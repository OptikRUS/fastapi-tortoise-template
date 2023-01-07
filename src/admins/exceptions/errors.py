from common.exceptions import BaseBadRequestError

"""
Ошибки админки
"""


class AdminSelfMatchError(BaseBadRequestError):
    """
    Ошибка редактирования самого себя
    """
    message: str = "Недоступно для себя."
    reason: str = "self_match_error"
