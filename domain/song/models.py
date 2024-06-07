from pydantic import BaseModel, Field


class Song(BaseModel):
    """Модель песни"""

    name: str = Field(max_length=100)
    text: str # TODO Продолжить расписывать модель песни (донастроить poetry (добавить линтеры) и читать доку Pydantic).
