from datetime import datetime

from tortoise import fields


class TimeBasedMixin:
    created_at: datetime = fields.DatetimeField(description="Дата создания", auto_now_add=True)
    updated_at: datetime = fields.DatetimeField(description="Дата обновления", auto_now=True)
