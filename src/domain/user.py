from src.domain.entity import Entity

class User(Entity):
    def __init__(self, name: str, age: int, city: str, occupation: str, company: str, investiment: float, entity_id=None):
        super().__init__(entity_id)
        self.name = name
        self.age = age
        self.city = city
        self.occupation = occupation
        self.company = company
        self.investiment = investiment
        print(f"User created with ID: {self.id}")