from typing import Union
import uuid
from fastapi import FastAPI, HTTPException

from src.domain.user import User
from src.presentation.user_data_mode_response import UserDataModelResponse
from src.presentation.user_data_model_request import UserDataModelRequest

app = FastAPI(title="Policy Service")

@app.get("/")
def read_root():
    return { "Hello": "World" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return { "item_id": item_id, "q": q }

@app.post("/users/", response_model=UserDataModelResponse)
async def create(request: UserDataModelRequest):
    try:
        user = User(request.name,
                    request.age,
                    request.city,
                    request.occupation,
                    request.company,
                    request.investiment)
        
        data_model = UserDataModelResponse(
            Id=user.id,
            name=user.name,
            age=user.age,
            city=user.city,
            occupation=user.occupation,
            company=user.company,
            investiment=user.investiment
        )

        return data_model
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
