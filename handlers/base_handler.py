from models.solicitation import Solicitation
from .base_handler import BaseHandler

class BaseHandler:
    _next_handler: BaseHandler = None

    def __init__(self) -> None:
        pass

    def set_next_handler(self, handler: BaseHandler) -> BaseHandler:
        self._next_handler = handler
        return self._next_handler

    def handle(self, solicitation: Solicitation) -> Solicitation:
        if self._next_handler is not None:
            self._next_handler.handle(solicitation)
        return solicitation;
