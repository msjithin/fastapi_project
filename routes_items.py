
from main import app
from database import items
from models import Item 
from fastapi import HTTPException

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

