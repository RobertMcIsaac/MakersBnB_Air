class Space:

    def __init__(self, name, description, price, user_ID):
        self.name = name
        self.description = description
        self.price = price
        self.user_ID = user_ID

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.name}, {self.description}, {self.price}, {self.user_ID})"