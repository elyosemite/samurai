from data_access.account_repository import AccountRepository
from handlers import BaseHandler
from actions import SingUp
from models.solicitation import Solicitation

class SignUpHandler(BaseHandler):
    def __init__(self, repository: AccountRepository) -> None:
        self.__repository = repository

    def handle(self, solicitation: Solicitation) -> Solicitation:
        if solicitation.token.key == "--create-account" | solicitation.token.key == "--create" | solicitation.token.key == "-c":
            account = SingUp(solicitation.token.value)
            solicitation.account = account
            solicitation.approved = True
            return solicitation
        else:
            return super().handle(solicitation)
