from abc import ABC, abstractmethod
from models.solicitation import Solicitation
from typing import Optional

class BaseHandler(ABC):

    _next_handler: Optional['BaseHandler'] = None
    
    def __init__(self) -> None:
        pass

    def set_next_handler(self, handler: Optional['BaseHandler']) -> 'BaseHandler':
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, solicitation: Solicitation) -> Solicitation:
        if self._next_handler is not None:
            return self._next_handler.handle(solicitation)
        else:
            return None
