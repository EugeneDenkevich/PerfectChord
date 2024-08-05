from typing import List, Optional, Union
from uuid import UUID

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncEngine

from backend.domain.auth.constants import LIMIT_REFRESH_TOKENS
from backend.domain.auth.exceptions import RefreshTokenNotFoundError
from backend.domain.auth.models import RefreshToken
from backend.domain.user.models import User
from backend.gateways.db.sql_gateway import SQLGateway
from backend.infrastructure.postgresql.models.refresh_token import (
    RefreshToken as RefreshTokenTable,
)
from backend.infrastructure.postgresql.models.user import User as UserTable


class PostgreSQLGateway(SQLGateway):
    """Реализвация интерфейса гейтвея для работы с PostgreSQL"""

    def __init__(self, engine: AsyncEngine) -> None:
        self.engine = engine

    async def save_user(self, user: User) -> User:
        """
        Создать пользователя

        :param user: Пользователь.
        :return: Пользователь.
        """

        async with self.engine.begin() as conn:
            query = (
                insert(UserTable)
                .values(
                    id=user.id,
                    username=user.username,
                    email=user.email,
                    password_hashed=user.password_hashed,
                    created_at=user.created_at,
                    updated_at=user.updated_at,
                    is_active=user.is_active,
                )
            )
            await conn.execute(query)

        return user

    async def get_user_or_none(
        self,
        id: Optional[UUID] = None,
        email: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Optional[User]:
        """
        Получить пользователя или None

        :param id: Id пользователя.
        :param email: Почта пользователя.
        :param username: Username пользователя.
        :return: Пользователь или None.
        """

        async with self.engine.begin() as conn:
            if id:
                query = select(UserTable).where(UserTable.id == id)
            elif email:
                query = select(UserTable).where(UserTable.email == email)
            elif username:
                query = select(UserTable).where(UserTable.username == username)
            cursor = await conn.execute(query)
            row = cursor.fetchone()
            if not row:
                return None
            return User.model_validate(row)

    async def get_users(
        self,
        limit: Union[int, None],
        offset: Union[int, None],
    ) -> List[User]:
        async with self.engine.begin() as conn:
            query = select(UserTable)
            if limit:
                query = query.limit(limit)
            if offset:
                query = query.offset(offset)
            cursor = await conn.execute(query)
            users = cursor.fetchall()
            return [User.model_validate(user) for user in users]

    async def get_refresh_token(self, id: Optional[UUID] = None) -> RefreshToken:
        async with self.engine.begin() as conn:
            query = select(RefreshTokenTable).where(RefreshTokenTable.id == id)
            cursor = await conn.execute(query)
            row = cursor.fetchone()
            if not row:
                raise RefreshTokenNotFoundError()
            return RefreshToken.model_validate(row)

    async def delete_refresh_token(self, user_id: Optional[UUID] = None) -> None:
        async with self.engine.begin() as conn:
            query = (
                delete(RefreshTokenTable)
                .where(RefreshTokenTable.user_id == user_id)
            )
            await conn.execute(query)

    async def delete_old_refresh_tokens(self, user_id: Optional[UUID] = None) -> None:
        async with self.engine.begin() as conn:
            subquery = (
                select(RefreshTokenTable)
                .filter(RefreshTokenTable.user_id == user_id)
                .order_by(RefreshTokenTable.created_at.desc())
                .offset(LIMIT_REFRESH_TOKENS - 1)
                .subquery()
            )
            query = (
                delete(RefreshTokenTable)
                .where(RefreshTokenTable.id.in_(select(subquery.c.id)))
            )
            await conn.execute(query)

    async def save_refresh_token(self, refresh_token: RefreshToken) -> None:
        async with self.engine.begin() as conn:
            query = (
                insert(RefreshTokenTable)
                .values(
                    id=refresh_token.id,
                    expired_at=refresh_token.expired_at,
                    created_at=refresh_token.created_at,
                    updated_at=refresh_token.updated_at,
                    user_id=refresh_token.user_id,
                )
            )
            await conn.execute(query)















    async def get_user_by_id(self, user_id: UUID) -> User:  # type: ignore[empty-body]
        ...

    async def update_user(  # type: ignore[empty-body]
        self,
        user_id: UUID,
        email: str | None,
        hashed_password: str | None,
    ) -> User:
        ...

    async def delete_user(self, user_id: UUID) -> None:  # type: ignore[empty-body]
        ...
