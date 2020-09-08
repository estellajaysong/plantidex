import requests
import imagehash
from io import BytesIO
from PIL import Image as PilImage
from pydantic import BaseModel
from typing import ClassVar, Optional, List

from base_models import QuerySizeEnum, image_size_map, image_directory
from .connection import db
from .base import BaseMongoDB
import base64


class Size(BaseModel):
    height: int
    width: int
    byte_size: int


class Image(BaseMongoDB):
    col_name: ClassVar[str] = 'images'

    plant_id: str
    file_name: str
    size: Size

    @classmethod
    async def search_by_text_or_size(
        cls, text: Optional[str], size: QuerySizeEnum
    ) -> List['Image']:
        """ Find images by file name or size or combination """

        query = {}
        if text:
            # Filter so the file_name contains the substring text
            query['file_name'] = {'$regex': text}
        if size:
            # Filter so the length of the image (the larger of image width and
            # image height) is within the range specified in image_size_map

            length_range = {'$gte': image_size_map[size].min_px}

            # Large images do not have a max length, so filter max length only
            # when applicable
            if image_size_map[size].max_px:
                length_range['$lte'] = image_size_map[size].max_px

            query['$or'] = [
                {
                    'size.height': length_range,
                    '$expr': {'$gte': ['$size.height', '$size.width']},
                },
                {
                    'size.width': length_range,
                    '$expr': {'$gte': ['$size.width', '$size.height']},
                },
            ]

        images = []
        async for raw in db[cls.col_name].find(query):
            images.append(cls(**raw))
        return images

    @classmethod
    async def search_by_image(
        cls, url: Optional[str], attachment: str
    ) -> List['Image']:
        """ Find similar images by comparing image hashes """

        similar_images = []
        if url:
            response = requests.get(url)
            og_image_hash = imagehash.average_hash(
                PilImage.open(BytesIO(response.content))
            )
        elif attachment:
            og_image_hash = imagehash.average_hash(
                PilImage.open(BytesIO(base64.b64decode(attachment)))
            )
        for image in await cls.find_all():
            compare_image_hash = imagehash.average_hash(
                PilImage.open(f'{image_directory}/{image.file_name}')
            )
            difference = og_image_hash - compare_image_hash
            if difference <= 10:
                similar_images.append(image)

        return similar_images
