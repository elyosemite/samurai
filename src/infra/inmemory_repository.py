import uuid
from typing import Type, List, Optional, Generic, TypeVar
from src.domain import AggregateRoot
from .mapper import Mapper

T = TypeVar('T', bound=AggregateRoot)
D = TypeVar('D')

class InMemoryRepository(Generic[T, D]):
    def __init__(self, aggregate_class: Type[T], mapper: Mapper[T, D]):
        self.aggregate_class = aggregate_class
        self.mapper = mapper
        self._storage: List[D] = []
    
    def save(self, aggregate: T) -> None:
        data_model: D = self.mapper.to_data_model(aggregate)
        self._storage.append(data_model)
    
    def find_by_id(self, aggregate_id: uuid.UUID) -> Optional[T]:
        for data in self._storage:
            if hasattr(data, 'id') and data.id == aggregate_id:
                return self.mapper.from_data_model(data)
        return None