from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


def datetime_now() -> datetime:
    return datetime.now(timezone.utc)


class Base(BaseModel):
    """Базовая модель"""

    id: Optional[UUID] = Field(default_factory=uuid4)
    created_at: Optional[datetime] = Field(default_factory=datetime_now)
    updated_at: Optional[datetime] = Field(default_factory=datetime_now)

    model_config = ConfigDict(
        extra="ignore",
        from_attributes=True,
        frozen=False,
        strict=True,
    )
