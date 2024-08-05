from pydantic import BaseModel, Field


class LoginInput(BaseModel):
    """Модель для входа в аккаунт."""

    email: str = Field(max_length=256)
    password: str = Field(min_length=8, max_length=256)


class AccessToken(BaseModel):
    """Токен доступа пользователя"""

    access_token: str
