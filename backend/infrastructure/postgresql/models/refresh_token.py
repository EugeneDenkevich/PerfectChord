from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from backend.infrastructure.postgresql.models.user import User


class RefreshToken(Base):
    """Таблица refresh токенов."""

    __tablename__ = "refresh_tokens"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    """Идентификатор токена."""
    expired_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )
    """Время окончания действия токена."""
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    """Дата создания пользователя"""
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    """Статус активности пользователя."""
    user_id: Mapped[UUID] = mapped_column(Uuid, ForeignKey("users.id"))
    """Id пользователя."""
    user: Mapped["User"] = relationship(back_populates="refresh_tokens")
    """Пользователь, которому принадлежит токен"""
