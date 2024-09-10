class User:

    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    
    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email}, {self.password})"   