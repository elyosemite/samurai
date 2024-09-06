from typing import Union

from fastapi import FastAPI
import uvicorn

from src.presentation.item import Item

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

'''
Estudo a partir do Hashtag Programação
'''

sales_items = {
    1: { "item": "lata 01", "unit_price": 4, "quantity": 90 },
    2: { "item": "lata 02", "unit_price": 3, "quantity": 50 },
    3: { "item": "lata 03", "unit_price": 1, "quantity": 20 },
    4: { "item": "lata 04", "unit_price": 8, "quantity": 70 }
}

@app.get("/sales")
def sales():
    return { "sales": sales_items }

@app.get("/sales/{sale_id}")
def sales_item(sale_id: int):
    if sale_id in sales_items:
        return sales_items[sale_id]
    else:
        return { "message": "error"}

# @app.post("/sales")
# def add_item(item: Item):
#     for _, item_value in sales_item.items():
#         if any(Item.name.lower() in str(value).lower() for value in item_value.values()):

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
