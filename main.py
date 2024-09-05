from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    username: str
    email: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get_user/")
def get_user(user: User):
    if not user.username or not user.email:
        raise HTTPException(status_code=400, detail="Invalid user data")
    return {"username": user.username, "email": user.email}
