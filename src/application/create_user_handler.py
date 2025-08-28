
from src.application.create_user_request import CreateUserRequest
from src.domain.user import User

class CreateUserHandler:
    def __init__(self):
        pass

    def Handler(self, request: CreateUserRequest):
        user = User(
            name=request.name,
            age=30,
            city="Unknown",
            occupation="Unknown",
            company="Unknown",
            investiment=0.0
        )
        return {"status": "User created", "user": user}