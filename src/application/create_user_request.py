from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name: str
    age: int
    city: str
    occupation: str
    company: str
    investiment: float