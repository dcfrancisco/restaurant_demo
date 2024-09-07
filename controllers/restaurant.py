from fastapi import APIRouter, HTTPException
from typing import List
from models.restaurant import Restaurant
from services.restaurant import (
    find_all,
    find_by_id,
    save,
    delete_by_id,
    exists_by_id,
)

router = APIRouter()


@router.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Restaurant Service API"}


# FastAPI routes
@router.get("/restaurants", response_model=List[Restaurant], tags=["Restaurants"])
async def get_restaurants():
    return await find_all()


@router.get("/restaurants/{id}", response_model=Restaurant, tags=["Restaurants"])
async def get_restaurant(id: str):
    restaurant = await find_by_id(id)
    if not restaurant:
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    return restaurant


@router.delete("/restaurants/{id}", tags=["Restaurants"])
async def delete_restaurant(id: str):
    if not await exists_by_id(id):
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    await delete_by_id(id)
    return {"message": f"Restaurant with id {id} has been deleted"}


@router.post("/restaurants", response_model=Restaurant, tags=["Restaurants"])
async def save_restaurant(restaurant: Restaurant):
    if await exists_by_id(restaurant.id):
        raise HTTPException(
            status_code=400, detail=f"Restaurant with id {restaurant.id} already exists"
        )
    return await save(restaurant)


@router.put("/restaurants/{id}", response_model=Restaurant, tags=["Restaurants"])
async def replace_restaurant(id: str, updated_restaurant: Restaurant):
    if not await exists_by_id(id):
        raise HTTPException(
            status_code=404, detail=f"Restaurant with id {id} not found"
        )
    await delete_by_id(id)  # Remove the old entry
    return await save(updated_restaurant)  # Save the new entry
