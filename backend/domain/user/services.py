from typing import Annotated

from fastapi import Depends
from passlib.handlers.pbkdf2 import pbkdf2_sha256

from backend.domain.user.models import User


class UserService:
    """Сервис сущности User"""

    @staticmethod
    def _hash_password(password: str) -> str:
        return pbkdf2_sha256.hash(password)

    def create(
        self,
        username: str,
        email: str,
        password: str,
    ) -> User:
        return User(
            username=username,
            email=email,
            password_hashed=self._hash_password(password),
        )


def build_user_service() -> UserService:
    return UserService()


UserServiceD = Annotated[UserService, Depends(build_user_service)]
