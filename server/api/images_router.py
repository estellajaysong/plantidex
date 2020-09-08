from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, AnyHttpUrl, Field
from typing import List
from base_models import QuerySizeEnum
from mongo_models import Image

images_router = APIRouter()


class ImageGetOutput(BaseModel):
    image: Image


class ImageGetList(BaseModel):
    images: List[Image]


class ImagePostInput(BaseModel):
    url: AnyHttpUrl = None
    attachment: str = Field(default=None, description='Base64 string')


@images_router.get('/search', response_model=ImageGetList)
async def search_images(text: str = None, size: QuerySizeEnum = None):
    """ Search images by file name or size or combination """

    if not text and not size:
        images = await Image.find_all()
    else:
        images = await Image.search_by_text_or_size(text=text, size=size)

    return {'images': images}


@images_router.post('/search', response_model=ImageGetList)
async def search_by_image(image: ImagePostInput):
    """ Search for similar images by image url or Base64 string"""

    if not image.url and not image.attachment:
        raise HTTPException(
            status_code=422,
            detail='Image url or attachment required',
        )
    images = await Image.search_by_image(
        url=image.url, attachment=image.attachment
    )

    return {'images': images}


@images_router.get('/{image_id}', response_model=ImageGetOutput)
async def get_image(image_id: str):
    """ Get an image """

    image = await Image.find_by_id(id=image_id)

    if image:
        return {'image': image}
    else:
        raise HTTPException(
            status_code=404,
            detail=f'Image with id {image_id} could not be found',
        )


@images_router.get('/', response_model=ImageGetList)
async def get_all_images():
    """ Get list of all images """

    images = await Image.find_all()

    return {'images': images}
