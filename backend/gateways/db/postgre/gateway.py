from uuid import UUID

from backend.domain.user.models import User
from backend.gateways.db.sql_gateway import SQLGateway


class PostgreGateway(SQLGateway):
    """Реализвация интерфейса гейтвея для работы с PostgreSQL"""

    async def save_user(  # type: ignore[empty-body]
        self,
        email: str,
        hashed_password: str,
    ) -> User:
        ...

    async def get_user_by_id(self, user_id: UUID) -> User:  # type: ignore[empty-body]
        ...
