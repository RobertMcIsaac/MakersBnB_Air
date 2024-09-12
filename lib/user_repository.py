from lib.space import Space
from lib.user import User
import hashlib

def pass_hash(password):
    binary_password = password.encode("utf-8")
    return hashlib.sha256(binary_password).hexdigest()

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def create_user(self, user):
        row = self._connection.execute('select * from users where username = %s', [user.username])
        # print(row)
        if row == []:
            row = self._connection.execute('select * from users where email = %s', [user.email])
            if row == []:
                if len(user.password) >= 8:            
                    if any(elem in '!@$%&' for elem in user.password) == True:
                        self._connection.execute('insert into users (username, email, password) values (%s, %s, %s)', [user.username, user.email, pass_hash(user.password)])
                    else:
                        raise Exception("This password does not comply with requirements! Must have at least one special character")
                else:
                    raise Exception("This password does not comply with requirements! Must have at least 8 characters")
            else:
                raise Exception("This email is already in use.")
        else:
            raise Exception("This username has been taken!")
        
    def check_password(self, username, password):
        # Check whether there is a user in the database with the given username
        # and a matching password hash, using a SELECT statement.
        rows = self._connection.execute(
            'select * from users where username = %s and password = %s',
            [username, pass_hash(password)])
        # If that SELECT finds any rows, the password is correct.
        return len(rows) > 0

    def get_user_details(self, username):
        rows = self._connection.execute('select * from users where username = %s', [username])
        if rows == []:
            return None
        else:
            row = rows[0]
            return User(row["id"], row["username"], row["email"], row["password"])
    
    def update_password(self, username, new_password):
        row = self._connection.execute('select * from users where username = %s', [username])
        if row != []:
            if len(new_password) >= 8:            
                if any(elem in '!@$%&' for elem in new_password) == True:
                    self._connection.execute('update users set password = %s where username = %s', [pass_hash(new_password), username])
                else:
                    raise Exception("This password does not comply with requirements! Must have at least one special character")
            else:
                raise Exception("This password does not comply with requirements! Must have at least 8 characters")
        else:
            raise Exception("User not found.")
        

    def delete_account(self, username):
        self._connection.execute('delete from users where username = %s', [username])
    
    def list_spaces_by_user(self, username):
        list_of_spaces = []
        user_id = self._connection.execute('select id from users where username = %s', [username])
        better_user_id = user_id[0]['id']
        rows = self._connection.execute('select * from spaces where user_id = %s',[better_user_id])
        # return rows
        for row in rows:
            item = Space(row["id"], row["name"], row["description"],row["price"], row["user_id"])
            list_of_spaces.append(item)
        return list_of_spaces

