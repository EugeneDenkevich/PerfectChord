import enum
from pathlib import Path
from tempfile import gettempdir

from pydantic_settings import BaseSettings, SettingsConfigDict

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Доступные уровни логов."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """Настройки приложения."""

    host: str = "0.0.0.0"
    port: int = 8000
    enable_doc: bool = True
    log_level: LogLevel = LogLevel.DEBUG
    workers_count: int = 1
    reload: bool = False
    environment: str = "prod"
    secrets_dir: str = "keys"
    public_key_path: str = "./keys/auth.key.pub"
    private_key_path: str = "./keys/auth.key"
    vader_path: str = "./vader"

    db_host: str = "localhost"
    db_name: str = "isa-main"
    db_port: int = 5432
    db_user: str = "isa-user"
    db_password: str = "isa-password"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="BACKEND_",
        env_file_encoding="utf-8",
    )


settings = Settings()
