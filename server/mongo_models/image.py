from pydantic import BaseModel, Field
from typing import List, ClassVar
from bson import ObjectId
from .base import BaseMongoDB, PydanticObjectId


class Size(BaseModel):
    height: int
    width: int
    byte_size: int


class Image(BaseMongoDB):
    col_name: ClassVar[str] = 'images'

    plant_id: str
    # tags: List[str] = []
    file_name: str
    # size: Size
