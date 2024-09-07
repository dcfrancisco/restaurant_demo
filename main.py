from fastapi import FastAPI
from controllers import restaurant

app = FastAPI()

# Include the router from restaurant_controller
app.include_router(restaurant.router)
