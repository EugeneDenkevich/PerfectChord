from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import Boolean, DateTime, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from backend.infrastructure.postgresql.models.refresh_token import RefreshToken


class User(Base):
    """Таблица пользователей."""

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True)
    """Идентификатор пользователя."""
    username: Mapped[str] = mapped_column(String(36), nullable=False, unique=True)
    """Юзернейм пользователя."""
    email: Mapped[str] = mapped_column(String(256), nullable=False, unique=True)
    """Почта пользователя."""
    password_hashed: Mapped[str] = mapped_column(String(256), nullable=False)
    """Хеш пароля пользователя."""
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
    """Дата обновления пользователя"""
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )
    """Статус активности пользователя."""
    refresh_tokens: Mapped["RefreshToken"] = relationship(back_populates="user")
    """Рефреш токены пользователя."""
