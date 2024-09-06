class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.__account_balance = 0