from pydantic import BaseModel
from .connection import DB


class BaseMongoDB(BaseModel):

    @classmethod
    async def find_one(cls, id: str):
        resource = await DB[cls.col_name].find_one({'id': id})
        return resource

    @classmethod
    async def find(cls):
        resources = await DB[cls.col_name].find({})
        return resources