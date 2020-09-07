from pydantic import BaseModel
from .query_size_enum import QuerySizeEnum


class Range(BaseModel):
    min_px: int
    max_px: int = None


image_size_map = {
    QuerySizeEnum.SMALL: Range(min_px=0, max_px=499),
    QuerySizeEnum.MEDIUM: Range(min_px=500, max_px=999),
    QuerySizeEnum.LARGE: Range(min_px=1000, max_px=None),
}


image_directory = 'images'