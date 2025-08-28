from uuid import UUID
from pydantic import BaseModel

class CreateUserResponse(BaseModel):
    id : UUID
    name: str
    age: int
    city: str
    occupation: str
    company: str
    investiment: float