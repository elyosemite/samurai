from models.user import User

class Account:
    def __init__(self, user: User) -> None:
        self.user = user
