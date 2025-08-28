from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Policy Service")

class User(BaseModel):
    name: str
    age: int
    city: str
    occupation: str
    company: str
    investiment: float

yuri = User(name="Yuri Melo", age=27, city="New York", occupation="Staff Engineer", company="CloudBeholder", investiment=1000.0)
julio = User(name="Julio Miguel", age=28, city="Los Angeles", occupation="Senior Software Engineer", company="CluodBeholder", investiment=1500.0)
thamyris = User(name="Thamyres Melo", age=22, city="San Francisco", occupation="Principal Software Engineer", company="CloudBeholder", investiment=1200.0)

@app.get("/")
def read_root():
    return { "Hello": "World" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return { "item_id": item_id, "q": q }

@app.get("/user")
def read_item():
    thamyris.investiment += 100
    return thamyris
