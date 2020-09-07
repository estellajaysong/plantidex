from pydantic import BaseModel
from typing import ClassVar, Optional, List
from base_models import QuerySizeEnum
from .connection import db
from .base import BaseMongoDB


class Size(BaseModel):
    height: int
    width: int
    byte_size: int


class Image(BaseMongoDB):
    col_name: ClassVar[str] = 'images'

    plant_id: str
    file_name: str
    size: Size

    @classmethod
    async def search_by_text_or_size(cls, text: Optional[str], size: QuerySizeEnum) -> List['Image']:
        """ Find images by file name or size or combination """
        query = {}
        if text:
            query['file_name'] = {'$regex': text}

        images = []
        async for raw in db[cls.col_name].find(query):
            images.append(cls(**raw))
        return images
