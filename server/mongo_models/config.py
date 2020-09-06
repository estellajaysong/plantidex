from typing import Optional
from pydantic import BaseSettings


class Config(BaseSettings):
    host: str = 'mongo'
    port: int = 27017
    db_name: str = 'identifi'

    class Config:
        env_prefix = 'MONGO_'


config = Config()
