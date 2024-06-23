
from typing import List
from uuid import UUID

from backend.domain.user.models import User
from backend.gateways.db.builders import SQLGateway


def hash_password_or_none(password: str | None) -> str | None:
    if password:
        return hash_password(password)
    return None


def hash_password(password: str) -> str:
    # TODO Посмотреть реализацию в Mercury
    return password[::-1]


class AddUserUseCase:
    """Добавление нового пользователя"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(
        self,
        email: str,
        password: str,
    ) -> User:
        return await self.sql_gateway.save_user(
            email=email,
            hashed_password=hash_password(password),
        )


class GetUserByIdUseCase:
    """Получение нового пользователя по его id"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(self, user_id: UUID) -> User:
        return await self.sql_gateway.get_user_by_id(
            user_id=user_id,
        )


class GetUsersUseCase:
    """Получение пользователей"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(
        self,
        limit: int | None,
        offset: int | None,
    ) -> List[User]:
        return await self.sql_gateway.get_users(limit=limit, offset=offset)


class UpdateUserUseCase:
    """Обновление пользователя"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(
        self,
        user_id: UUID,
        email: str | None,
        password: str | None,
    ) -> User:
        return await self.sql_gateway.update_user(
            user_id=user_id,
            email=email,
            hashed_password=hash_password_or_none(password),
        )


class DeleteUserUseCase:
    """Удаление пользователя"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(
        self,
        user_id: UUID,
    ) -> None:
        await self.sql_gateway.delete_user(user_id=user_id)
