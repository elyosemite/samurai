from models.user import User
from data_access import AccountRepository

class SingUp:
    def __init__(self, repository: AccountRepository):
        self.__repository = repository

    def create_account(self, name: str) -> User:
        account = User(name)
        self.__repository.insert_account(account)
        return account
