from pydantic import BaseModel
from typing import Optional


class Product(BaseModel):
    id:int
    name: str
    price: float
    description: str
    quantity: int
    
    
        