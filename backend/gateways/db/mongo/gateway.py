from uuid import UUID

from backend.domain.models import Song
from backend.gateways.db.nosql_gateway import NoSQLGateway


class MongoGateway(NoSQLGateway):
    """Реализвация интерфейса гейтвея для работы с MongoDB"""

    async def save_song(   # type: ignore[empty-body]
        self,
        title: str,
        author: str | UUID,
        body: dict[int, str],
    ) -> Song:
        ...
