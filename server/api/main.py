from fastapi import FastAPI
from mongo_models import DB
from .images_router import images_router


app = FastAPI()

app.include_router(images_router, prefix='/images')


@app.on_event('startup')
async def startup_events():
    pass


@app.get('/health', include_in_schema=False)
async def health():
    return 'OK'
