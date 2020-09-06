from fastapi import FastAPI
from loguru import logger
from mongo_models import config, seed_db
from .images_router import images_router


app = FastAPI()

app.include_router(images_router, prefix='/images')


@app.on_event('startup')
async def startup_events():
    logger.info('Seeding database')
    await seed_db()
    pass


@app.get('/health', include_in_schema=False)
async def health():
    return 'OK'
