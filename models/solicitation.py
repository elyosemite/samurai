from models.sam_token import SamToken
from models.solicitation_type import SolicitationType

class Solicitation:
    def __init__(self, token: SamToken, solicitation_type: SolicitationType) -> None:
        self.token = token
        self.errorMessages = []
        self.approved = None
        self.solicitation_type = solicitation_type
        self.account = None