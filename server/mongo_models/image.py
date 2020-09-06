from pydantic import BaseModel
from typing import ClassVar
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
