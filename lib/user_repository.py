from lib.user import *
class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        self._connection.execute('insert into users (username, email, password) values (%s, %s, %s)', [user.username, user.email, user.password])

    def get_user_details(self, username):
        rows = self._connection.execute('select * from users where username = %s', [username])
        row = rows[0]
        return User(row["id"], row["username"], row["email"], row["password"])
