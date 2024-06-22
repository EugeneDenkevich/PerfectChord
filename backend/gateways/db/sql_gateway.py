from abc import ABC, abstractmethod
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
