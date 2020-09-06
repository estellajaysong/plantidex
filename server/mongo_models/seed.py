from .constants import plants
from .plant import Plant


async def seed_db():
    for plant in plants:
        print(plant)