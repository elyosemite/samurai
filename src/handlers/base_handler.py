from abc import ABC, abstractmethod
from models.solicitation import Solicitation
from typing import Optional

class BaseHandler(ABC):
    def __init__(self) -> None:
        self._next_handler: Optional[BaseHandler] = None

    def set_next_handler(self, handler: Optional['BaseHandler']) -> 'BaseHandler':
        self._next_handler = handler
        return self._next_handler

    @abstractmethod
    def handle(self, solicitation: Solicitation) -> Solicitation:
        print(self._next_handler)
        if self._next_handler is not None:
            self._next_handler.handle(solicitation)
        return solicitation
