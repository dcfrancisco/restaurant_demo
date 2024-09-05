from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from typing import List
import os

# Initialize the FastAPI app
app = FastAPI()

# MongoDB connection setup
mongodb_host = os.getenv("MONGODB_HOST", "localhost")
mongodb_port = int(os.getenv("MONGODB_PORT", 27017))
mongodb_database = os.getenv("MONGODB_DATABASE", "restaurant_db")

client = AsyncIOMotorClient(f"mongodb://{mongodb_host}:{mongodb_port}")
db = client[mongodb_database]
restaurant_collection = db["restaurants"]


# Pydantic model for Restaurant
class Restaurant(BaseModel):
    id: str
    name: str
    address: str  # Updated from "location" to "address"


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


# FastAPI routes
@app.get("/restaurants", response_model=List[Restaurant])
async def get_restaurants():
    return await find_all()


@app.get("/restaurants/{id}", response_model=Restaurant)
async def get_restaurant(id: str):
    restaurant = await find_by_id(id)
    if not restaurant:
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    return restaurant


@app.delete("/restaurants/{id}")
async def delete_restaurant(id: str):
    if not await exists_by_id(id):
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    await delete_by_id(id)
    return {"message": f"Restaurant with id {id} has been deleted"}


@app.post("/restaurants", response_model=Restaurant)
async def save_restaurant(restaurant: Restaurant):
    if await exists_by_id(restaurant.id):
        raise HTTPException(
            status_code=400, detail=f"Restaurant with id {restaurant.id} already exists"
        )
    return await save(restaurant)


@app.put("/restaurants/{id}", response_model=Restaurant)
async def replace_restaurant(id: str, updated_restaurant: Restaurant):
    if not await exists_by_id(id):
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    await delete_by_id(id)  # Remove the old entry
    return await save(updated_restaurant)  # Save the new entry
