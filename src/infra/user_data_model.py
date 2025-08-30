from dataclasses import dataclass
import uuid

@dataclass
class UserDataModel:
    id: uuid.UUID
    first_name: str
