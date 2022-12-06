from cli.user import User

class AccountRepository:
    def __init__(self) -> None:
        self.__accounts = []
    
    def insert_account(self, account: User):
        self.__accounts.append(account)

    def find_account(self, name: str) -> User:
        for account in self.__accounts:
            if account.name == name:
                return account
        return None
