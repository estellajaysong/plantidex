from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from mongo_models import Image

images_router = APIRouter()


class ImageGetOutput(BaseModel):
    image: Image


class ImageGetList(BaseModel):
    images: List[Image]


@images_router.get('/search')
async def search_images(text: str):
    """ Search images """

    images = await Image.find_by_file_name_contains(substring=text)

    return {'images': images}


@images_router.get('/{image_id}', response_model=ImageGetOutput)
async def get_image(image_id: str):
    """ Get an image """

    image = await Image.find_one(id=image_id)

    return {'image': image}


@images_router.get('/', response_model=ImageGetList)
async def get_all_images():
    """ Get list of all images """

    images = await Image.find()

    return {'images': images}
