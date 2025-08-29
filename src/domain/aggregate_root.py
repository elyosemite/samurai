from ast import List
from src.domain.domain_event import DomainEvent
from src.domain.domain_event_dispatcher import DomainEventDispatcher
from src.domain.entity import Entity

class AggregateRoot(Entity):
    def __init__(self, entity_id = None):
        super().__init__(entity_id)
        self._events: List[DomainEvent] = []
    
    def raise_event(self, event: DomainEvent):
        self._events.append(event)

    @property
    def get_events(self) -> tuple:
        return tuple(self._events)
    
    def dispatch_events(self):
        for event in self._events:
            DomainEventDispatcher.dispatch(event)
        self._events.clear()