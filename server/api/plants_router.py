from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from mongo_models import Plant

plants_router = APIRouter()


class PlantGetOutput(BaseModel):
    Plant: Plant


class PlantGetList(BaseModel):
    plants: List[Plant]


@plants_router.get('/search')
async def search_plants(text: str):
    """ Search plants """

    plants = await Plant.find_by_text()

    return {'plants': plants}


@plants_router.get('/{plant_id}', response_model=PlantGetOutput)
async def get_plant(plant_id: str):
    """ Get an plant """

    plant = await Plant.find_one(id=plant_id)

    return {'plant': plant}


@plants_router.get('/', response_model=PlantGetList)
async def get_all_plants():
    """ Get list of all plants """

    plants = await Plant.find()

    return {'plants': plants}
