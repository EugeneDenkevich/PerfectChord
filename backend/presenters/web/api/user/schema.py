from pydantic import BaseModel, EmailStr, Field

from backend.presenters.web.api.schema import Pagination


class CreateUserInput(BaseModel):
    """Инпут для создания пользователя."""

    username: str = Field(max_length=36)
    email: EmailStr
    password: str = Field(min_length=8, max_length=36)


class GetUsersInput(Pagination):
    """Инпут для получения списка пользователей."""
