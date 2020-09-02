from motor.motor_asyncio import AsyncIOMotorClient

DB = AsyncIOMotorClient(host='mongo', port=27017).plantidex
