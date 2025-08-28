from abc import ABC
from uuid import UUID
import uuid

class Entity(ABC):
    def __init__(self, entity_id: UUID = None):
        if entity_id and not isinstance(entity_id, uuid.UUID):
            raise ValueError(f"entity_id must be a UUID, goooooot {type(entity_id)}: {entity_id}")

        self._id = entity_id or uuid.uuid4()
        print(f"Entity created with ID: {self._id}")
    
    @property
    def id(self) -> uuid.UUID:
        return self._id
    
    def __eq__(self, other):
        if isinstance(other, Entity):
            return self._id == other._id
        return False
    
    def __hash__(self):
        return hash(self._id)
    