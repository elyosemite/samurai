from src.domain.user import User
from src.infra.mapper import Mapper
from src.infra.user_data_model import UserDataModel

class UserMapper(Mapper[User, UserDataModel]):
    def to_data_model(self, aggregate: User) -> UserDataModel:
        return UserDataModel(id=aggregate.id, first_name=aggregate.first_name)
    
    def from_data_model(self, data: UserDataModel) -> User:
        return User(id=data.id, first_name=data.first_name, last_name="", active=False)