from motor.motor_asyncio import AsyncIOMotorClient
import os
from models.restaurant import Restaurant

# MongoDB connection setup
mongodb_host = os.getenv("MONGODB_HOST", "localhost")
mongodb_port = int(os.getenv("MONGODB_PORT", 27017))
mongodb_database = os.getenv("MONGODB_DATABASE", "restaurant_db")

client = AsyncIOMotorClient(f"mongodb://{mongodb_host}:{mongodb_port}")
db = client[mongodb_database]
restaurant_collection = db["restaurants"]


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
