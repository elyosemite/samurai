from cli.menu import Menu
from data_access.account_repository import AccountRepository
from handlers.sing_in_handler import SingInHandler
from models.solicitation import Solicitation
from models.sam_token import Token
from models.solicitation_type import SolicitationType

class StartUp:
    def __init__(self) -> None:
        self.__menu = Menu()

    def run(self):
        print(f'Starting Samurai CLI')
        self.__menu.show()
        value = str(input("Type a command (number or shortcut): "))

        repository = AccountRepository()
        token = Token("--create-account", "yuri_conta")
        solicitation = Solicitation(token, SolicitationType.SING_UP)

        chain_of_responsability = SingInHandler(repository).set_next_handler()

        # match value:
        #     case "-c" | "--create-account" | "-create":
        #         print("Criando conta")
            
        #     case "-i" | "--sing-in" | "--sing-in-acount":
        #         print("Entrando na sua conta")
            
        #     case "-t" | "--tranfer-cash":
        #         print("Transferindo dinheiro para outra conta ...")

        #     case "-s" | "--show-balancer":
        #         print("Seu saldo")