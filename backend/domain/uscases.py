from uuid import UUID

from backend.domain.models import Body, Song
from backend.gateways.db.gateway import DBGateway


class AddSongUseCase:
    """Юзер кейс добавления новой песни"""

    def __init__(
        self,
        db_gateway: DBGateway,
    ) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, title: str, author: str | UUID, body: Body) -> Song:
        return await self.db_gateway.save_song(
            title=title,
            author=(
                await self.db_gateway.get_user_by_id(user_id=author)
                if isinstance(author, UUID) else author
            ),
            body=body,
        )
