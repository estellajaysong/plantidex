from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from mongo_models import Plant

plants_router = APIRouter()


class PlantGetOutput(BaseModel):
    plant: Plant


class PlantGetList(BaseModel):
    plants: List[Plant]


@plants_router.get('/{plant_id}', response_model=PlantGetOutput)
async def get_plant(plant_id: str):
    """ Get an plant """

    plant = await Plant.find_by_id(id=plant_id)

    if plant:
        return {'plant': plant}
    else:
        raise HTTPException(
            status_code=404,
            detail=f'Plant with id {plant_id} could not be found',
        )


@plants_router.get('/', response_model=PlantGetList)
async def get_all_plants():
    """ Get list of all plants """

    plants = await Plant.find_all()

    return {'plants': plants}
