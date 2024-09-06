from data_access.account_repository import AccountRepository
from handlers import BaseHandler
from actions import SingUp
from models.solicitation import Solicitation
from models.solicitation_type import SolicitationType

class SignUpHandler(BaseHandler):
    def __init__(self, repository: AccountRepository) -> None:
        self.__repository = repository

    def handle(self, solicitation: Solicitation) -> Solicitation:
        if solicitation.token.key == "--create-account" | solicitation.token.key == "--create" | solicitation.token.key == "-c":
            account = SingUp(solicitation.token.value)
            solicitation.account = account
            solicitation.approved = True
            solicitation.solicitation_type = SolicitationType.SING_UP
            return solicitation
            
        return super().handle(solicitation)
