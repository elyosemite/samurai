from actions import SignIn
from cli.user import User
from data_access.account_repository import AccountRepository
from models.solicitation import Solicitation
from models.solicitation_type import SolicitationType
from .base_handler import BaseHandler

class SingInHandler(BaseHandler):
    def __init__(self, repository: AccountRepository) -> None:
        self.__repository = repository

    def handle(self, solicitation: Solicitation) -> Solicitation:
        if solicitation.token.key == "--sing-in-account" | solicitation.token.key == "--sing-in" | solicitation.token.key == "-s":
            account: User = SignIn(self.__repository).log_in(solicitation.token.name)

            if account != None:
                solicitation.account = account
                solicitation.approved = True
                solicitation.solicitation_type = SolicitationType.SING_IN
                return solicitation
            
            solicitation.account = account
            solicitation.approved = False
            solicitation.solicitation_type = SolicitationType.LOG_IN_ERROR
            return solicitation

        return super().handle(solicitation);
