from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from base_models import QuerySizeEnum
from mongo_models import Image

images_router = APIRouter()


class ImageGetOutput(BaseModel):
    image: Image


class ImageGetList(BaseModel):
    images: List[Image]


class ImagePostInput(BaseModel):
    url: str = None
    attachment: str = None


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
    """ Search similar images by image """
    # if not image_url or attachment:
    #     raise HTTPException(
    #     status_code=400,
    #     detail='No image_url ')
    images = await Image.search_by_image(url=image.url, attachment=image.attachment)

    # hash = imagehash.average_hash(Image.open('test.jpg'))
    return {'images': images}
