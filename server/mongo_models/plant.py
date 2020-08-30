from pydantic import BaseModel
from typing import List

class Plant(BaseModel):
    scientific_name: str
    aliases: List[str]