from lib.user import User
class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        row = self._connection.execute('select * from users where username = %s', [user.username])
        # print(row)
        if row == []:
            if len(user.password) >= 8:            
                if any(elem in '!@$%&' for elem in user.password) == True:
                    self._connection.execute('insert into users (username, email, password) values (%s, %s, %s)', [user.username, user.email, user.password])
                else:
                    raise Exception("This password does not comply with requirements! Must have at least one special character")
            else:
                    raise Exception("This password does not comply with requirements! Must have at least 8 characters")
        else:
            raise Exception("This username has been taken!")

    def get_user_details(self, username):
        rows = self._connection.execute('select * from users where username = %s', [username])
        row = rows[0]
        return User(row["id"], row["username"], row["email"], row["password"])
    
    def update_password(self, username, new_password):
        row = self._connection.execute('select * from users where username = %s', [username])
        if row != []:
            if len(new_password) >= 8:            
                if any(elem in '!@$%&' for elem in new_password) == True:
                    self._connection.execute('update users set password = %s where username = %s', [new_password, username])
                else:
                    raise Exception("This password does not comply with requirements! Must have at least one special character")
            else:
                raise Exception("This password does not comply with requirements! Must have at least 8 characters")
        else:
            raise Exception("User not found.")