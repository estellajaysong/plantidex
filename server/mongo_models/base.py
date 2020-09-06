from pydantic import BaseModel, validator, Field
from shortuuid import ShortUUID
from typing import Dict, Any
import json
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
from .connection import db
from .utils import timestamp_now, JSONEncoder


class BaseMongoDB(BaseModel):
    id: str = None
    created_at: int = None
    updated_at: int = None

    @validator('id', pre=True, always=True, check_fields=False)
    def set_id(cls, id):
        return id or ShortUUID().random(length=10)

    @validator('created_at', pre=True, always=True, check_fields=False)
    def set_created_at(cls, timestamp):
        return timestamp or timestamp_now()

    @validator('updated_at', pre=True, always=True, check_fields=False)
    def set_updated_at(cls, timestamp):
        return timestamp or timestamp_now()

    @classmethod
    async def find_one(cls, query: Dict[Any, Any] = dict()):
        resource = await db[cls.col_name].find_one(query)
        return resource

    @classmethod
    async def find(cls, query: Dict[Any, Any] = dict()):
        resources = await db[cls.col_name].find(query)
        return resources

    @classmethod
    async def insert_many(cls, resources):
        # json_resources = [json.dumps(resource, cls=JSONEncoder) for resource in resources]
        json_resources = [jsonable_encoder(resource) for resource in resources]
        await db[cls.col_name].insert_many(json_resources)
