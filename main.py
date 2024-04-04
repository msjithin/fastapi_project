# main.py
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    
app = FastAPI()

items = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
async def create_item(item: str):
    items.append(item)
    return items 

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = items[item_id]
    return item 
