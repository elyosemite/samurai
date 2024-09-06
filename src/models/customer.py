from models import Address

class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.__addresses: Address = []

    def insert_address(self, city: str, state: str) -> None:
        self.__addresses.append(Address(city, state))

    def show_address(self) -> None:
        for address in self.__addresses:
            print(f'{address.city}-{address.state}')
    