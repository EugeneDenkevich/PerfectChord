from dataclasses import dataclass

from sqlalchemy import URL

from backend.infrastructure.base_config import BaseDatabase
from backend.settings import settings


@dataclass
class SettingsPostgresql(BaseDatabase):
    """Конфигурация базы данных Postgres."""

    def get_connection_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            database=self.name,
        )


def load_database_settings() -> SettingsPostgresql:
    """Загружает конфигурацию для базы данных."""

    return SettingsPostgresql(
        host=settings.db_host,
        port=settings.db_port,
        name=settings.db_name,
        user=settings.db_user,
        password=settings.db_password,
    )
