import uuid

class IncreaseUserInvestmentHandler:
    def __init__(self, user_identifier: uuid.UUID, investment_value):
        self.user_identifier = user_identifier
        self.investment_value = investment_value