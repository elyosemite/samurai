
from src.application.create_user_request import CreateUserRequest
from src.domain.user import User

class CreateUserHandler:
    def __init__(self):
        pass

    def Handler(self, request: CreateUserRequest):
        user = User(
            name=request.name,
            age=request.age,
            city=request.city,
            occupation=request.occupation,
            company=request.company,
            investiment=request.investiment
        )
        return {"status": "User created", "user": user}