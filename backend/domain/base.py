from datetime import datetime, timezone
from typing import Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, model_validator


def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

DateTimeAt = Annotated[datetime, Field(default_factory=datetime_now)]


class Base(BaseModel):
    """Базовая модель"""

    id: UUID = Field(default_factory=uuid4)
    created_at: DateTimeAt
    updated_at: DateTimeAt

    class Config:
        validate_assignment = True

    @model_validator(mode="after")  # type: ignore[arg-type]
    @classmethod
    def update_updated_at(cls, obj: "Base") -> "Base":
        obj.model_config["validate_assignment"] = False
        obj.updated_at = datetime_now()
        obj.model_config["validate_assignment"] = True
        return obj
