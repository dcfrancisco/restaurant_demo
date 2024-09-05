from pydantic import BaseModel


class Restaurant(BaseModel):
    id: str
    name: str
    address: str
