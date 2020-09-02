from fastapi import FastAPI
from mongo_models import DB

app = FastAPI()


@app.on_event('startup')
async def startup_events():
    pass


@app.get('/health', include_in_schema=False)
async def health():
    return 'OK'
