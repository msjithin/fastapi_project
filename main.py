# main.py
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel

class Item(BaseModel):
    text: str 
    is_done: bool = False
    
app = FastAPI()

items = []

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
async def create_item(item: Item):
    items.append(item)
    return  f"Item {item} created"

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail=f"Item with id={item_id} not found")
    else :
        item = items[item_id]
        return item 
