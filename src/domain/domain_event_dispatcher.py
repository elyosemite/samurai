from typing import Callable

class DomainEventDispatcher:
    _handlers = {}

    @classmethod
    def register_handler(cls, event_type: str, handler: Callable):
        if event_type not in cls._handlers:
            cls._handlers[event_type] = []
        cls._handlers[event_type].append(handler)

    @classmethod
    def dispatch(cls, event):
        event_type = event.event_type
        if event_type in cls._handlers:
            for handler in cls._handlers[event_type]:
                handler(event)