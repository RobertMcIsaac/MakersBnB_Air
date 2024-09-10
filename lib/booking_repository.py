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
    
    def create(self, booking):
        self._connection.execute('INSERT INTO bookings (date_booked, booking_status, user_id, space_id) VALUES (%s, %s, %s, %s)', [
                                booking.date_booked, booking.booking_status, booking.user_id, booking.space_id])
        return None

    def confirm_booking(self, id):
        self._connection.execute(
        'UPDATE bookings SET booking_status = %s WHERE id = %s', 
        ['confirmed', id])
        return None
