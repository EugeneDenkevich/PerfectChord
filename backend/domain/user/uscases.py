from typing import List, Union
from uuid import UUID

from backend.domain.user.exceptions import EmailExistsError, UsernameExistsError
from backend.domain.user.models import User
from backend.domain.user.services import UserService
from backend.gateways.db.builders import SQLGateway


class CreateUserUseCase:
    """Добавление нового пользователя"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
        user_service: UserService,
    ) -> None:
        self.sql_gateway = sql_gateway
        self.user_service = user_service

    async def __call__(
        self,
        username: str,
        email: str,
        password: str,
    ) -> User:
        if await self.sql_gateway.get_user_or_none(email=email):
            raise EmailExistsError()
        if await self.sql_gateway.get_user_or_none(username=username):
            raise UsernameExistsError()
        user = self.user_service.create(
            username=username,
            email=email,
            password=password,
        )
        return await self.sql_gateway.save_user(user)


class GetUsersUseCase:
    """Получение пользователей"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(
        self,
        limit: Union[int, None],
        offset: Union[int, None],
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
            hashed_password=password,
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
