from typing import Annotated

from fastapi import Depends

from backend.domain.uscases import AddSongUseCase
from backend.gateways.db.gateway import DBGatewayD


def build_add_song_usecase(db_gateway: DBGatewayD) -> AddSongUseCase:
    return AddSongUseCase(db_gateway=db_gateway)


AddSongUseCaseD = Annotated[AddSongUseCase, Depends(build_add_song_usecase)]
