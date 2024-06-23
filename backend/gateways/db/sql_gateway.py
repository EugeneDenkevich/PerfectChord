from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from backend.domain.user.models import User


class SQLGateway(ABC):
    """Гейтвей для работы с SQL базами данных"""

    @abstractmethod
    async def save_user(self, email: str, hashed_password: str) -> User:
        ...

    @abstractmethod
    async def get_user_by_id(self, user_id: UUID) -> User:
        ...

    @abstractmethod
    async def get_users(self, limit: int | None, offset: int | None) -> List[User]:
        ...

    @abstractmethod
    async def update_user(
        self,
        user_id: UUID,
        email: str | None,
        hashed_password: str | None,
    ) -> User:
        ...

    @abstractmethod
    async def delete_user(self, user_id: UUID) -> None:
        ...
