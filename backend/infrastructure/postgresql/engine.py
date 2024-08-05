from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from backend.infrastructure.postgresql.config_loader import SettingsPostgresql
from backend.infrastructure.postgresql.models.base import Base


@asynccontextmanager
async def get_engine(settings: SettingsPostgresql) -> AsyncGenerator[AsyncEngine, None]:
    try:
        engine = create_async_engine(
            url=settings.get_connection_url(),
            future=True,
            pool_pre_ping=True,
        )

        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield engine

    finally:
        await engine.dispose()
