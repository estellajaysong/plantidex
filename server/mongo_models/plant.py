from typing import ClassVar, Optional
from .base import BaseMongoDB
from .connection import db


class Plant(BaseMongoDB):
    col_name: ClassVar[str] = 'plants'

    scientific_name: str

    @classmethod
    async def find_by_scientific_name(cls, scientific_name: str) -> Optional['Plant']:
        """ Find one plant by its scientific name """

        raw = await db[cls.col_name].find_one({'scientific_name': scientific_name})
        return cls(**raw) if raw else None
