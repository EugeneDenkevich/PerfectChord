
from backend.domain.auth.constants import REFRESH_EXPIRATION
from backend.domain.auth.exceptions import UserNotFoundError
from backend.domain.auth.models import Tokens
from backend.domain.auth.services import AuthService
from backend.gateways.db.builders import SQLGateway


class GetTokensUseCase:
    """Получение токенов"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
        auth_service: AuthService,
    ) -> None:
        self.sql_gateway = sql_gateway
        self.auth_service = auth_service

    async def __call__(
        self,
        email: str,
        password: str,
    ) -> Tokens:
        user = await self.sql_gateway.get_user_or_none(email=email)
        if not user:
            raise UserNotFoundError()
        self.auth_service.ensure_can_access(user=user, password=password)
        await self.sql_gateway.delete_old_refresh_tokens(user_id=user.id)
        refresh_token = self.auth_service.create_refresh_token(user_id=user.id)
        await self.sql_gateway.save_refresh_token(refresh_token=refresh_token)
        access_t = self.auth_service.generate_access_token(user=user)
        refresh_t = self.auth_service.generate_refresh_token(
            refresh_token=refresh_token,
        )
        return Tokens(
            access_token=access_t,
            refresh_token=refresh_t,
            refresh_token_expiration_time=int(REFRESH_EXPIRATION.total_seconds()),
        )


class RefreshTokensUseCase:
    """Обновление токенов"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
        auth_service: AuthService,
    ) -> None:
        self.sql_gateway = sql_gateway
        self.auth_service = auth_service

    async def __call__(
        self,
        refresh_t: str,
    ) -> Tokens:
        refresh_token = self.auth_service.decode_refresh_token(refresh_t=refresh_t)
        await self.sql_gateway.get_refresh_token( # Проверка, есть ли такой токен в БД.
            id=refresh_token.id,
        )
        user = await self.sql_gateway.get_user_or_none(id=refresh_token.user_id)
        if not user:
            raise UserNotFoundError()
        new_refresh_token = self.auth_service.create_refresh_token(user_id=user.id)
        await self.sql_gateway.delete_refresh_token(user_id=user.id)
        await self.sql_gateway.save_refresh_token(refresh_token=new_refresh_token)
        access_t = self.auth_service.generate_access_token(user=user)
        refresh_t = self.auth_service.generate_refresh_token(
            refresh_token=new_refresh_token,
        )
        return Tokens(
            access_token=access_t,
            refresh_token=refresh_t,
            refresh_token_expiration_time=int(REFRESH_EXPIRATION.total_seconds()),
        )
