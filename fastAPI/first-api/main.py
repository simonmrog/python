from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

# dummy database
items = []

# pydantic models
class Item(BaseModel):
  item_id: str
  name: str
  price: float
  discount: bool = False

# endpoints
@app.get('/')
def hello_world():
  return "Welcome to the Items Crud API!"


@app.get("/items")
def get_items():
  return {
    "status": "ok",
    "items": items
  }

@app.get("/items/{item_id}")
def get_item_by_id(item_id: str, q1: str = None, q2: str = None):
  return {
    "item_id": item_id,
    "q1": q1,
    "q2": q2
  }


@app.post("/items/add")
def add_item(item: Item = None):
  if item != None:
    items.append(item)
  return {
    "status": "ok",
    "items": items
  }