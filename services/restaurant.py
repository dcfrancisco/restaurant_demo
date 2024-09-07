from models.restaurant import Restaurant
from database import restaurant_collection


# Repository functions
async def find_all():
    return await restaurant_collection.find().to_list(100)


async def find_by_id(restaurant_id: str):
    return await restaurant_collection.find_one({"id": restaurant_id})


async def save(restaurant: Restaurant):
    await restaurant_collection.insert_one(restaurant.dict())
    return restaurant


async def delete_by_id(restaurant_id: str):
    await restaurant_collection.delete_one({"id": restaurant_id})


async def exists_by_id(restaurant_id: str):
    return (
        await restaurant_collection.count_documents({"id": restaurant_id}, limit=1) > 0
    )
