from src.domain.events import UserInvestimentDecreasedEvent, UserInvestimentIncreasedEvent
from src.domain.user import User

def test_user_entity():
    user = User(
        name = "Yuri Melo",
        age = 30,
        city = "New York",
        occupation = "Chemical Engineer",
        company = "TechCorp",
        investiment = 0.0
    )

    assert user.name == "Yuri Melo"
    assert user.age == 30
    assert user.city == "New York"
    assert user.occupation == "Chemical Engineer"
    assert user.company == "TechCorp"
    assert user.investiment == 0.0
    assert isinstance(user, User)

def test_user_investiment_management():
    user = User(
        name = "Jane Smith",
        age = 28,
        city = "San Francisco",
        occupation = "Software Engineer",
        company = "Innovatech",
        investiment = 1000.0
    )
    user.add_investiment(500.0)
    user.decrease_investiment(200.0)
    assert user.investiment == 1300.0
    assert len(user.get_events) == 2
    assert isinstance(user.get_events[0], UserInvestimentIncreasedEvent)
    assert isinstance(user.get_events[1], UserInvestimentDecreasedEvent)
    assert user.get_events[0].amount == 500.0
    assert user.get_events[1].amount == 200.0
    

def test_user_investiment_decrease():
    user = User(
        name = "Alice Johnson",
        age = 35,
        city = "Los Angeles",
        occupation = "Product Manager",
        company = "Creatives Inc",
        investiment = 2000.0
    )
    user.decrease_investiment(300.0)
    assert len(user.get_events) == 1
    assert isinstance(user.get_events[0], UserInvestimentDecreasedEvent)
    assert user.get_events[0].amount == 300.0
    assert user.investiment == 1700.0