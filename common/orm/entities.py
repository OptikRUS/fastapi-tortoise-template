from .filters import QBuilder
from .annotations import AnnotationBuilder


class BaseRepo:
    """
    Базовый репозиторий
    """
    q_builder: QBuilder
    a_builder: AnnotationBuilder
