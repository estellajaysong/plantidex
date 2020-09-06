from pydantic import BaseModel
from typing import List
from .base import BaseMongoDB


class Plant(BaseMongoDB):
    scientific_name: str
    # aliases: List[str]
    # characteristics: List[str]
