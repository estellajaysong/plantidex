from typing import ClassVar, Optional
from .base import BaseMongoDB


class Plant(BaseMongoDB):
    col_name: ClassVar[str] = 'plants'

    scientific_name: str
    # aliases: List[str]
    # characteristics: List[str]

    @classmethod
    async def find_by_scientific_name(cls, scientific_name: str) -> Optional['Plant']:
        raw = await cls.find_one({'scientific_name': scientific_name})
        return cls(**raw) if raw else None
