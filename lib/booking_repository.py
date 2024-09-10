from lib.booking import Booking

class BookingRepository():
    def __init__(self, db_connection):
        self._connection = db_connection
    def all(self):
        rows = self._connection.execute('SELECT * from bookings')
        all_bookings = []
        for row in rows:
            item = Booking(row['id'], row['date_booked'], row['booking_status'], row['user_id'], row['space_id'])
            all_bookings.append(item)
        return all_bookings
    
    # def all(self):
    #     rows = self._connection.execute('SELECT * from artists')
    #     artists = []
    #     for row in rows:
    #         item = Artist(row["id"], row["name"], row["genre"])
    #         artists.append(item)
    #     return artists