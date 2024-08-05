from typing import Annotated

from fastapi import Depends

from backend.domain.auth.services import AuthServiceD
from backend.domain.auth.uscases import (
    GetTokensUseCase,
    RefreshTokensUseCase,
)
from backend.gateways.db.builders import SQLGatewayD


def build_get_tokens_user_usecase(
    sql_gateway: SQLGatewayD,
    auth_service: AuthServiceD,
) -> GetTokensUseCase:
    return GetTokensUseCase(sql_gateway=sql_gateway, auth_service=auth_service)


GetTokensUseCaseD = Annotated[GetTokensUseCase, Depends(build_get_tokens_user_usecase)]


def build_refresh_roken_usecase(
    sql_gateway: SQLGatewayD,
    auth_service: AuthServiceD,
) -> RefreshTokensUseCase:
    return RefreshTokensUseCase(sql_gateway=sql_gateway, auth_service=auth_service)


RefreshTokensUseCaseD = Annotated[
    RefreshTokensUseCase,
    Depends(build_refresh_roken_usecase),
]
