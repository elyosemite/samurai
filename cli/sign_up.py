from cli.user import User

class SingUp:
    def __init__(self):
        pass

    def create_account(self, name: str) -> User:
        return User(name)