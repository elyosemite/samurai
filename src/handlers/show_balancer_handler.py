from handlers.base_handler import BaseHandler
from models.solicitation import Solicitation

class ShowBalancerHandler(BaseHandler):
    def __init__(self) -> None:
        pass

    def handle(self, solicitation: Solicitation) -> Solicitation:
        print("I am the balancer...")
        return super().handle(solicitation)
