from typing import Annotated

from fastapi import Depends

from backend.domain.user.uscases import (
    AddUserUseCase,
)
from backend.gateways.db.builders import SQLGatewayD


def build_add_user_usecase(
    sql_gateway: SQLGatewayD,
) -> AddUserUseCase:
    return AddUserUseCase(sql_gateway=sql_gateway)


AddUserUseCaseD = Annotated[AddUserUseCase, Depends(build_add_user_usecase)]
