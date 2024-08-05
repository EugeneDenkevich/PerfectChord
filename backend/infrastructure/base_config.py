from abc import ABC, abstractmethod
from dataclasses import dataclass

from sqlalchemy import URL


@dataclass
class BaseDatabase(ABC):
    """Базовая конфигурация базы данных."""

    host: str
    port: int
    name: str
    user: str
    password: str

    @abstractmethod
    def get_connection_url(self) -> URL:
        raise NotImplementedError
