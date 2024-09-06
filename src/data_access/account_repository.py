from typing import List, Optional
from models.user import User
from models.account import Account

class AccountRepository:
    def __init__(self) -> None:
        self.__accounts: List[Account] = []
    
    def insert_account(self, account: Account):
        self.__accounts.append(account)

    def find_account(self, username: str) -> Optional['User']:
        for account in self.__accounts:
            if account.user.name == username:
                return account.user
        return None
