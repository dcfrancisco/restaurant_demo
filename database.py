import os
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection setup
mongodb_host = os.getenv("MONGODB_HOST", "localhost")
mongodb_port = int(os.getenv("MONGODB_PORT", 27017))
mongodb_database = os.getenv("MONGODB_DATABASE", "restaurant_db")

# Create a client and get the database
client = AsyncIOMotorClient(f"mongodb://{mongodb_host}:{mongodb_port}")
db = client[mongodb_database]

# Export the collections that can be used in services
restaurant_collection = db["restaurants"]
