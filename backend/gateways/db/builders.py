from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncEngine

from backend.gateways.db.mongo.gateway import MongoGateway
from backend.gateways.db.nosql_gateway import NoSQLGateway
from backend.gateways.db.postgre.gateway import PostgreSQLGateway
from backend.gateways.db.sql_gateway import SQLGateway
from backend.infrastructure.postgresql.config_loader import load_database_settings
from backend.infrastructure.postgresql.engine import get_engine


async def build_postgresql_engine() -> AsyncEngine:
    db_settings = load_database_settings()
    async with get_engine(db_settings) as engine:
        return engine


PostgreSQLEngineD = Annotated[AsyncEngine, Depends(build_postgresql_engine)]


def build_sql_gateway(
    engine: PostgreSQLEngineD,
) -> PostgreSQLGateway:
    return PostgreSQLGateway(engine)


SQLGatewayD = Annotated[SQLGateway, Depends(build_sql_gateway)]


def build_nosql_gateway() -> MongoGateway:
    return MongoGateway()


NoSQLGatewayD = Annotated[NoSQLGateway, Depends(build_nosql_gateway)]
