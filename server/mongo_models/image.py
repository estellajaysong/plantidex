from pydantic import BaseModel
from typing import List, ClassVar
from bson import ObjectId
from .base import BaseMongoDB


class Size(BaseModel):
    height: int
    width: int
    byte_size: int


class Image(BaseMongoDB):
    col_name: ClassVar[str] = 'images'

    # plant_id: ObjectId
    # tags: List[str] = []
    file_name: str
    size: Size
