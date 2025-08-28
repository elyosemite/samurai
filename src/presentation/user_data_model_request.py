from pydantic import BaseModel

class UserDataModelRequest(BaseModel):
    name: str
    age: int
    city: str
    occupation: str
    company: str
    investiment: float