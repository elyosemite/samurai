from src.domain.aggregate_root import AggregateRoot
from src.domain.events import UserInvestimentDecreasedEvent, UserInvestimentIncreasedEvent

class User(AggregateRoot):
    def __init__(self, name: str, age: int, city: str, occupation: str, company: str, investiment: float, entity_id=None):
        super().__init__(entity_id)
        self.name = name
        self.age = age
        self.city = city
        self.occupation = occupation
        self.company = company
        self.investiment = investiment
        print(f"User created with ID: {self.id}")
    
    def add_investiment(self, amount: float):
        if amount <= 0:
            raise ValueError("Investiment amount must be positive.")
        self.investiment += amount
        self.raise_event(UserInvestimentIncreasedEvent(self.id, amount))
    
    def decrease_investiment(self, amount: float):
        if amount <= 0:
            raise ValueError("Investiment amount must be positive.")
        if amount > self.investiment:
            raise ValueError("Cannot decrease investiment below zero.")
        self.investiment -= amount
        self.raise_event(UserInvestimentDecreasedEvent(self.id, amount))