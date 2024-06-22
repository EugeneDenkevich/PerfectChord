
from backend.domain.user.models import User
from backend.gateways.db.builders import SQLGateway


class AddUserUseCase:
    """Добавление нового пользователя"""

    def __init__(
        self,
        sql_gateway: SQLGateway,
    ) -> None:
        self.sql_gateway = sql_gateway

    async def __call__(
        self,
        email: str,
        password: str,
    ) -> User:
        return await self.sql_gateway.save_user(
            email=email,
            hashed_password=self._hash_password(password),
        )

    def _hash_password(self, password: str) -> str:
        # TODO Посмотреть реализацию в Mercury
        return password[::-1]
