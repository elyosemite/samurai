import uuid
from src.domain.domain_event import DomainEvent

class UserInvestimentIncreasedEvent(DomainEvent):
    def __init__(self, aggregate_id: uuid.UUID, amount: float):
        super().__init__(aggregate_id)
        self.amount = amount

class UserInvestimentDecreasedEvent(DomainEvent):
    def __init__(self, aggregate_id: uuid.UUID, amount: float):
        super().__init__(aggregate_id)
        self.amount = amount
