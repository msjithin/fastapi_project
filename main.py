# main.py
from fastapi import FastAPI, HTTPException
from models import Item, User, UUID
from database import db

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

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{users_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist.")
    
    