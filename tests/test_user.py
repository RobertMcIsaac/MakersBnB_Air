from lib.user import *

"""
User constructs with a username, email and password
"""
def test_user_constructs_unique_username():
    user = User(1, "Avnita", "ab@example.com", "Password£123")
    assert user.id == 1
    assert user.username == "Avnita"
    assert user.email == "ab@example.com"
    assert user.password == "Password£123"
    assert user.spaces == []
    assert user.bookings == []
    # try:
    #     user2 = User(2, "Avnita", "po@example.com", "kjfein%121")
    # except Exception as excinfo:
    #     pytest.fail(f"Unexpected excepion raised: {excinfo}")

"""
We can format user to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "Avnita", "ab@example.com", "Password£123", [], [])
    assert str(user) == "User(1, Avnita, ab@example.com, Password£123)"


"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Avnita", "ab@example.com", "Password£123", [], [])
    user2 = User(1, "Avnita", "ab@example.com", "Password£123", [], [])
    assert user1 == user2