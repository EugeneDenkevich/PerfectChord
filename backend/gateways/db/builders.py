from typing import Annotated

from fastapi import Depends

from backend.gateways.db.mongo.gateway import MongoGateway
from backend.gateways.db.nosql_gateway import NoSQLGateway
from backend.gateways.db.postgre.gateway import PostgreGateway
from backend.gateways.db.sql_gateway import SQLGateway


def build_sql_gateway() -> PostgreGateway:
    return PostgreGateway()


SQLGatewayD = Annotated[SQLGateway, Depends(build_sql_gateway)]


def build_nosql_gateway() -> MongoGateway:
    return MongoGateway()


NoSQLGatewayD = Annotated[NoSQLGateway, Depends(build_nosql_gateway)]
