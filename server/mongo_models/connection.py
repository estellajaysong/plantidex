from motor.motor_asyncio import AsyncIOMotorClient
from .config import config

DB = AsyncIOMotorClient(host=config.host, port=config.port)[config.db_name]
