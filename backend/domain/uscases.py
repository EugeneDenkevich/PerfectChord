from typing import Annotated
from uuid import UUID

from fastapi import Depends

from backend.domain.models import Body, Song
from backend.gateways.db.gateway import DBGateway, DBGatewayD


class AddSongUseCase:
    async def __init__(
            self,
            db_gateway: DBGateway,
    ) -> None:
        self.db_gateway = db_gateway

    async def __call__(self, title: str, author: str | UUID, body: Body) -> Song:
        song = await self.db_gateway.save_song(
            title=title,
            author=(
                await self.db_gateway.get_user_by_id(user_id=author)
                if isinstance(author, UUID) else author
            ),
            body=body,
        )
        return song


def build_add_song_usecase(db_gateway: DBGatewayD):
    return AddSongUseCase(db_gateway=db_gateway)


AddSongUseCaseD = Annotated[AddSongUseCase, Depends(build_add_song_usecase)]
