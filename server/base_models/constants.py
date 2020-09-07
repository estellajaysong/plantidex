from pydantic import BaseModel
from query_size_enum import QuerySizeEnum


class Range(BaseModel):
    min_px: int
    max_px: int = None


image_size_map = {
    QuerySizeEnum.small: Range(min_px=0, max_px=499),
    QuerySizeEnum.medium: Range(min_px=500, max_px=999),
    QuerySizeEnum.large: Range(min_px=100, max_px=None)
}
