from pydantic import BaseModel, validator
from .connection import DB
from .utils import timestamp_now


class BaseMongoDB(BaseModel):
    created_at: int = None
    updated_at: int = None

    @validator('created_at', pre=True, always=True, check_fields=False)
    def set_created_at(cls, timestamp):
        return timestamp or timestamp_now()

    @validator('updated_at', pre=True, always=True, check_fields=False)
    def set_updated_at(cls, timestamp):
        return timestamp or timestamp_now()

    @classmethod
    async def find_one(cls, id: str):
        resource = await DB[cls.col_name].find_one({'id': id})
        return resource

    @classmethod
    async def find(cls):
        resources = await DB[cls.col_name].find({})
        return resources
