from datetime import datetime
from typing import Annotated, Optional
from uuid import UUID

import jwt
from dateutil.tz import UTC
from fastapi import Depends
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from backend.domain.auth.constants import ACCESS_EXPIRATION, REFRESH_EXPIRATION
from backend.domain.auth.credentials import PrivateKeyD, PublicKeyD
from backend.domain.auth.exceptions import (
    InvalidCredentialsError,
    InvalidRefreshTokenError,
    RefreshTokenExpiredError,
    UserNotActiveError,
)
from backend.domain.auth.models import RefreshToken
from backend.domain.user.models import User


class AuthService:
    """Сервис сущности Auth"""

    def __init__(self, public_key: bytes, private_key: bytes) -> None:
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def _verify_password(raw_password: str, password_hashed: str) -> str:
        return pbkdf2_sha256.verify(raw_password, password_hashed)

    def ensure_can_access(
        self,
        user: User,
        password: str,
    ) -> None:
        if not user.is_active:
            raise UserNotActiveError()

        password_match = self._verify_password(password, user.password_hashed)
        if not password_match:
            raise InvalidCredentialsError()
        return

    def decode_refresh_token(self, refresh_t: str) -> RefreshToken:
        try:
            payload = jwt.decode(
                jwt=refresh_t,
                key=self.public_key,
                algorithms=["RS256"],
            )
        except jwt.ExpiredSignatureError:
            raise RefreshTokenExpiredError()
        except jwt.InvalidTokenError:
            raise InvalidRefreshTokenError()

        return RefreshToken(
            id=UUID(payload["sub"]),
            user_id=UUID(payload["user_id"]),
            expired_at=datetime.fromtimestamp(payload["exp"], tz=UTC),
            created_at=datetime.fromtimestamp(payload["iat"], tz=UTC),
        )

    def create_refresh_token(self, user_id: Optional[UUID] = None) -> RefreshToken:
        return RefreshToken(user_id=user_id)

    def generate_access_token(self, user: User) -> str:
        return jwt.encode(
            payload={
                "sub": str(user.id),
                "email": user.email,
                "username": user.username,
                "reg_date": str(user.created_at),
                "upd_date": str(user.updated_at),
                "is_active": user.is_active,
                "type": "ACCESS_TOKEN",
                "iat": datetime.now(tz=UTC),
                "exp": datetime.now(tz=UTC) + ACCESS_EXPIRATION,
            },
            key=self.private_key,
            algorithm="RS256",
        )

    def generate_refresh_token(self, refresh_token: RefreshToken) -> str:
        return jwt.encode(
            payload={
                "sub": str(refresh_token.id),
                "user_id": str(refresh_token.user_id),
                "type": "REFRESH_TOKEN",
                "iat": datetime.now(tz=UTC),
                "exp": datetime.now(tz=UTC) + REFRESH_EXPIRATION,
            },
            key=self.private_key,
            algorithm="RS256",
        )

def build_auth_service(
    public_key: PublicKeyD,
    private_key: PrivateKeyD,
) -> AuthService:
    return AuthService(public_key=public_key, private_key=private_key)


AuthServiceD = Annotated[AuthService, Depends(build_auth_service)]
