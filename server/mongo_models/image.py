from pydantic import BaseModel
from typing import ClassVar, List
from .connection import db
from .base import BaseMongoDB


class Size(BaseModel):
    height: int
    width: int
    byte_size: int


class Image(BaseMongoDB):
    col_name: ClassVar[str] = 'images'

    plant_id: str
    # tags: List[str] = []
    file_name: str
    size: Size

    @classmethod
    async def find_by_file_name_contains(cls, substring: str) -> List['Image']:
        """ Find images by a substring that the file_name contains """

        images = []
        async for raw in db[cls.col_name].find({'file_name': {'$regex': substring}}):
            images.append(cls(**raw))
        return images
