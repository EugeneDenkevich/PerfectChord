from uuid import UUID

from backend.domain.models import Song
from backend.gateways.db.sql_gateway import SQLGateway


class PostgreGateway(SQLGateway):
    """Реализвация интерфейса гейтвея для работы с PostgreSQL"""

    async def get_user_by_id(self, user_id: UUID) -> Song:  # type: ignore[empty-body]
        ...
