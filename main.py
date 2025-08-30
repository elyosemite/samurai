from fastapi import FastAPI, HTTPException

from src.application.command_handler import CreateUserHandler
from src.application.command_handler import CreateUserRequest
from src.application.command_handler import CreateUserResponse

app = FastAPI(title="Policy Service")

@app.post("/users/", response_model=CreateUserResponse)
async def create(request: CreateUserRequest):
    try:
        handler = CreateUserHandler()
        return handler.Handler(request)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
