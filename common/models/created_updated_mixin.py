from datetime import datetime

from tortoise import fields


class TimeBasedMixin:
    created_at: datetime = fields.DatetimeField(description="Когда создано", auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(description="Когда обновлено", auto_now=True)
