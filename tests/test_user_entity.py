from src.domain.user import User

def test_user_entity():
    user = User(
        name = "John Doe",
        age = 30,
        city = "New York",
        occupation = "Chemical Engineer",
        company = "TechCorp",
        investiment = 0.0
    )

    assert user.name == "John Doe"
    assert user.age == 30
    assert user.city == "New York"
    assert user.occupation == "Chemical Engineer"
    assert user.company == "TechCorp"
    assert user.investiment == 0.0
