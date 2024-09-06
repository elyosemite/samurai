from models.user import User
from data_access.account_repository import AccountRepository

class SignIn:
    def __init__(self, repository: AccountRepository) -> None:
        self.__repository = repository

    def log_in(self, name: str) -> User:
        account = self.__repository.find_account(name)
        return account
