FROM python:3.11-alpine3.19

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /project

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry install --no-root --no-interaction

COPY ./scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/entrypoint.sh

COPY . .
RUN poetry install --no-root --no-interaction

ENTRYPOINT [ "/scripts/entrypoint.sh" ]
