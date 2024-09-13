from lib.space import Space

class SpaceRepository():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            space = Space(row["id"], row["name"], row["description"], row["price"], row["user_id"])
            spaces.append(space)
        return spaces
    
    def create(self, space: Space):
        rows = self._connection.execute("INSERT INTO spaces (name, description, price, user_id) VALUES (%s, %s, %s, %s) RETURNING id", [space.name, space.description, space.price, space.user_id])
        space = rows[0]
        return space["id"]
    
    # find with owner
    def find_with_user_id(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE user_id = %s", [id])
        return [Space(row["id"], row["name"], row["description"], row["price"], row["user_id"]) for row in rows]

    # find by space_id
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id = %s", [id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price"], row["user_id"])