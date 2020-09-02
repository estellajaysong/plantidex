from pydantic import BaseModel
from typing import List, ClassVar
from .base import BaseMongoDB

class Size(BaseModel):
    length: int
    width: int
    byte_size: int

class Image(BaseMongoDB):
    col_name: ClassVar[str] = 'images'

    plant_id: str
    tags: List[str] = []
    size: Size

