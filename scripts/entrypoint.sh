#!/bin/sh
poetry run python -m alembic -c /project/alembic.ini upgrade head
poetry run python -m backend
