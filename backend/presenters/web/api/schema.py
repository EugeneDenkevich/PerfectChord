
from typing import Optional

from pydantic import BaseModel, PositiveInt


class Pagination(BaseModel):
    """Пагинация."""

    limit: Optional[PositiveInt] = None
    offset: Optional[PositiveInt] = None
