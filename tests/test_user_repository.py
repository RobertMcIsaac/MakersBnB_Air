from lib.user import *
from lib.user_repository import *
import pytest

"""test creation of a new user record. username must be unique"""

# def test_create_unique_username(db_connection):
#     db_connection.seed("seeds/air_makersbnb_test.sql")
#     repository = UserRepository(db_connection)
#     repository.create_user(User(None, "Alex", "alexemail@email.com", "password1"))
#     try:
#         repository.create_user(User(None, "Alex", "dunno@gmail.com", "badpassword"))
#     except Exception as excinfo:
#         pytest.fail(f"Unexpected exception raised: {excinfo}")

"""test when we call user repository we can read their details"""
def test_read_user_details(db_connection):
    db_connection.seed("seeds/air_makersbnb_test.sql")
    repository = UserRepository(db_connection)
    user = repository.get_user_details("Alex")
    assert user == User(3, "Alex", "alex@example.com", "password£7£89")

