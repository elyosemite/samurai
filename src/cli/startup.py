from cli.menu import Menu
from data_access.account_repository import AccountRepository
from handlers.show_balancer_handler import ShowBalancerHandler
from handlers.sign_in_handler import SignInHandler
from models.solicitation import Solicitation
from models.sam_token import SamToken
from models.solicitation_type import SolicitationType

class StartUp:
    def __init__(self) -> None:
        self.__menu = Menu()

    def run(self):
        print(f'Starting Samurai CLI')
        self.__menu.show()
        value = str(input("Type a command (number or shortcut): "))

        repository = AccountRepository()

        splittedValue = value.split(" ")
        token_key   = splittedValue[0]
        token_value = splittedValue[1]

        token = SamToken(token_key, token_value)
        solicitation = Solicitation(token)

        balancer = ShowBalancerHandler()
        signInHandler = SignInHandler(repository)

        signInHandler.set_next_handler(balancer)
        
        signInHandler.handle(solicitation)
