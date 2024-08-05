from abc import ABC, abstractmethod
from typing import List, Optional, Union
from uuid import UUID

from backend.domain.auth.models import RefreshToken
from backend.domain.user.models import User


class SQLGateway(ABC):
    """Гейтвей для работы с SQL базами данных"""

    @abstractmethod
    async def save_user(self, user: User) -> User:
        ...

    @abstractmethod
    async def get_user_or_none(
        self,
        id: Optional[UUID] = None,
        email: Optional[str] = None,
        username: Optional[str] = None,
    ) -> Optional[User]:
        ...

    @abstractmethod
    async def get_users(
        self,
        limit: Union[int, None],
        offset: Union[int, None],
    ) -> List[User]:
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

    @abstractmethod
    async def get_refresh_token(self, id: Optional[UUID] = None) -> RefreshToken:
        ...

    @abstractmethod
    async def delete_refresh_token(self, user_id: Optional[UUID] = None) -> None:
        ...

    @abstractmethod
    async def delete_old_refresh_tokens(self, user_id: Optional[UUID] = None) -> None:
        ...

    @abstractmethod
    async def save_refresh_token(self, refresh_token: RefreshToken) -> None:
        ...
