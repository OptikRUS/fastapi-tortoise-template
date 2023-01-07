from .filters import QBuilder
from .annotations import AnnotationBuilder


class BaseRepo:
    q_builder: QBuilder
    a_builder: AnnotationBuilder
