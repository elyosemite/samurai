from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from src.domain import AggregateRoot

T = TypeVar('T', bound=AggregateRoot)
D = TypeVar('D')

class Mapper(ABC, Generic[T, D]):
    """
    Abstract base class for mapping between AggregateRoot and DataModel.
    """
    
    @abstractmethod
    def to_data_model(self, aggregate: T) -> D:
        """
        Map AggregateRoot to DataModel.
        """
        pass
    
    @abstractmethod
    def from_data_model(self, data: D) -> T:
        """
        Map DataModel back to AggregateRoot.
        """
        pass