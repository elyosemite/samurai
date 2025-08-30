from src.application.command_handler.create_user.create_user_request import CreateUserRequest
from src.application.command_handler.create_user.create_user_response import CreateUserResponse
from src.domain.user import User

from src.infra import InMemoryRepository

class CreateUserHandler:
    def __init__(self, InMemoryRepository = None):
        pass

    def Handler(self, request: CreateUserRequest) -> CreateUserResponse:
        user = User(
            name=request.name,
            age=request.age,
            city=request.city,
            occupation=request.occupation,
            company=request.company,
            investiment=request.investiment
        )
        
        return CreateUserResponse(
            id=user.id,
            name=user.name,
            age=user.age,
            city=user.city,
            occupation=user.occupation,
            company=user.company,
            investiment=user.investiment
        )