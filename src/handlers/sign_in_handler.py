from actions import SignIn
from models.user import User
from data_access.account_repository import AccountRepository
from models.solicitation import Solicitation
from models.solicitation_type import SolicitationType
from .base_handler import BaseHandler

class SignInHandler(BaseHandler):
    def __init__(self, repository: AccountRepository) -> None:
        super().__init__()
        self.__repository = repository

    def handle(self, solicitation: Solicitation) -> Solicitation:
        if solicitation.token.key == "--sign-in-account" or solicitation.token.key == "--sign-in" or solicitation.token.key == "-s":
            # account: User = SignIn(self.__repository).log_in(solicitation.token.value)

            # if account != None:
            #     solicitation.account = account
            #     solicitation.approved = True
            #     solicitation
            
            # solicitation.account = account
            # solicitation.approved = False
            # return solicitation

            super().handle(solicitation)
