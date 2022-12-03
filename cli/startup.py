from cli.menu import Menu

class StartUp:
    def __init__(self) -> None:
        self.__menu = Menu()

    def run(self):
        print(f'Starting Samurai CLI')
        self.__menu.show()
        value = str(input("Type a command (number or shortcut): "))

        match value:
            case "-c" | "--create-account" | "-create":
                print("Criando conta")
            
            case "-i" | "--sing-in" | "--sing-in-acount":
                print("Entrando na sua conta")
            
            case "-t" | "--tranfer-cash":
                print("Transferindo dinheiro para outra conta ...")

            case "-s" | "--show-balancer":
                print("Seu saldo")