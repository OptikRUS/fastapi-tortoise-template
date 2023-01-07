from typing import Optional, Any

from tortoise import Model
from tortoise.expressions import Q


class QBuilder:
    """
    Конструктор Q объектов
    """

    def __init__(self, model: type[Model]) -> None:
        self.model: type[Model] = model

    def __call__(
            self,
            or_filters: Optional[list[Q | dict[str, Any]]] = None,
            and_filters: Optional[list[Q | dict[str, Any]]] = None
    ) -> Q:
        _filter = Q()
        if or_filters:
            for or_filter in or_filters:
                if isinstance(or_filter, Q):
                    _filter |= or_filter
                else:
                    _filter |= Q(**or_filter)
        elif and_filters:
            for and_filter in and_filters:
                if isinstance(and_filter, Q):
                    _filter &= and_filter
                else:
                    _filter &= Q(**and_filter)
        return _filter
