import uuid
from pydantic import BaseModel

class UserDataModelResponse(BaseModel):
    Id: uuid.UUID
    name: str
    age: int
    city: str
    occupation: str
    company: str
    investiment: float