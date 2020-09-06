import os
import re
from PIL import Image as PIL_Image, UnidentifiedImageError
from loguru import logger
from .constants import plants
from .plant import Plant
from .image import Image, Size
from .connection import db


async def seed_db():
    """ Seed the plants and images in the db """
    # Check to see if db is empty
    logger.info("Seeding plants")
    # if await db[Plant.col_name].count_documents(filter={}):
    #     logger.info(f'Database is not empty: Skip seeding')
    #     return
    # # Seed plants
    # db_plants = [Plant(scientific_name=plant) for plant in plants]
    # await Plant.insert_many(resources=db_plants)
    # Seed images
    logger.info("Seeding images")
    images_dir = 'images'
    regex = re.compile('[^a-zA-Z\s\']')
    db_images = []
    for file_name in os.listdir(images_dir):
        # Remove the extension from the file name
        base_name = os.path.splitext(file_name)[0]
        # Remove non alphabet characters
        plant_name = regex.sub('', base_name)
        plant = await Plant.find_by_scientific_name(scientific_name=plant_name)
        if not plant:
            logger.warning(
                f'Could not find plant with scientific name {plant_name} to link to image '
                f'{file_name}: Skipping image'
            )
            continue
        file_path = f'{images_dir}/{file_name}'
        byte_size = os.path.getsize(filename=file_path)
        try:
            pil_image = PIL_Image.open(file_path)
        except UnidentifiedImageError:
            logger.warning(f'Unable to interpret file at {file_path}: Removing file')
            os.remove(path=file_path)
        width, height = pil_image.size

        db_image = Image(
            plant_id=plant.id,
            file_name=file_name,
            size=Size(height=height, width=width, byte_size=byte_size),
        )
        db_images.append(db_image)
    blah = await Image.insert_many(resources=db_images)
    print(blah)