from fastapi import FastAPI, HTTPException

from src.application.command_handler import CreateUserHandler
from src.application.command_handler import CreateUserRequest
from src.application.command_handler import CreateUserResponse
from src.domain.user import User

from src.infra.inmemory_repository import InMemoryRepository
from src.infra.user_data_model import UserDataModel
from src.infra.user_mapper import UserMapper

app = FastAPI(title="Policy Service")

@app.post("/users/", response_model=CreateUserResponse)
async def create(request: CreateUserRequest):
    try:
        mapper = UserMapper()

        repo = InMemoryRepository[User, UserDataModel](User, mapper)
        repo.save()

        handler = CreateUserHandler()

        return handler.Handler(request)
    except Exception as e:
        return HTTPException(status_code=400, detail=str(e))
