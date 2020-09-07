from pydantic import BaseModel
from typing import ClassVar, Optional, List
from base_models import QuerySizeEnum, image_size_map
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
    async def search_by_text_or_size(
        cls, text: Optional[str], size: QuerySizeEnum
    ) -> List['Image']:
        """ Find images by file name or size or combination """

        query = {}
        if text:
            query['file_name'] = {'$regex': text}
        if size:
            query['$or'] = [
                {
                    'size.height': {
                        '$gte': image_size_map[size].min_px,
                        '$lte': image_size_map[size].max_px,
                    },
                    '$expr': {'$gte': ['$size.height', '$size.width']},
                },
                {
                    'size.width': {
                        '$gte': image_size_map[size].min_px,
                        '$lte': image_size_map[size].max_px,
                    },
                    '$expr': {'$gte': ['$size.width', '$size.height']},
                },
            ]

        images = []
        async for raw in db[cls.col_name].find(query):
            images.append(cls(**raw))
        return images
