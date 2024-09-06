from data_access.account_repository import AccountRepository
from models.solicitation import Solicitation
from .base_handler import BaseHandler

class SignInHandler(BaseHandler):
    def __init__(self, repository: AccountRepository) -> None:
        super().__init__()
        self.__repository = repository

    def handle(self, solicitation: Solicitation) -> Solicitation:
        # Business Logic
        if solicitation.token.key == "--sign-in-account" or solicitation.token.key == "--sign-in" or solicitation.token.key == "-s":
            print("Done")
            # account: User = SignIn(self.__repository).log_in(solicitation.token.value)

            # if account != None:
            #     solicitation.account = account
            #     solicitation.approved = True
            #     solicitation
            
            # solicitation.account = account
            # solicitation.approved = False
            # return solicitation
        else:
            # or Delegate for another handler
            return super().handle(solicitation)
