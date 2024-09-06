from models.account import Account
from models.user import User
from models.sam_token import SamToken
from models.solicitation_type import SolicitationType

class Solicitation:
    def __init__(self, token: SamToken) -> None:
        self.token: SamToken = token
        self.errorMessages = []
        self.approved: bool = False
        self.account: Account