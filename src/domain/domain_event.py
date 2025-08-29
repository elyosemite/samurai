from abc import ABC
import uuid

class DomainEvent(ABC):
    def __init__(self, aggregate_id: uuid.UUID):
        self.aggregate_id = aggregate_id
        self.event_type = self.__class__.__name__
