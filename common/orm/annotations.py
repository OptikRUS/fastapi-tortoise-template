from tortoise import Model
from tortoise.expressions import Q, F
from tortoise.functions import Count, Max, Sum, Min, Avg


class AnnotationBuilder:
    """
    Конструктор аннотаций
    """

    def __init__(self, model: type[Model]) -> None:
        self.model: type[Model] = model

    def build_f(self, field: str | None = None) -> F:
        return F(field, field)

    def build_min(self, field: str | None, _filter: Q | None = None) -> Min:
        return Min(field, _filter=_filter)

    def build_sum(self, field: str | None, _filter: Q | None = None) -> Sum:
        return Sum(field, _filter=_filter)

    def build_max(self, field: str | None, _filter: Q | None = None) -> Max:
        return Max(field, _filter=_filter)

    def build_avg(self, field: str | None, _filter: Q | None = None) -> Avg:
        return Avg(field, _filter=_filter)

    def build_count(self, field: str | None, _filter: Q | None = None) -> Count:
        return Count(field, _filter=_filter)
