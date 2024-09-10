from lib.booking import Booking

class BookingRepository():
    def __init__(self, db_connection):
        self._connection = db_connection
    def all(self):
        rows = self._connection.execute('SELECT * from bookings ORDER BY id')
        all_bookings = []
        for row in rows:
            item = Booking(row['id'], row['date_booked'], row['booking_status'], row['user_id'], row['space_id'])
            all_bookings.append(item)
        return all_bookings
    
    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings \
                (date_booked, booking_status, user_id, space_id) \
                    VALUES (%s, %s, %s, %s) RETURNING id', 
                    [booking.date_booked, booking.booking_status, booking.user_id, booking.space_id]
                    )
        row = rows[0]
        # captures the booking id returned in SQL executed above with 'RETURNING id' and assigns it to the id attribute of booking (booking.id)
        booking.id = row['id']
        return booking
    
    # We should probably just initialise booking_status as 'pending' by default directly in Booking init method
    def confirm_booking(self, id):
        self._connection.execute(
            'UPDATE bookings SET booking_status = %s WHERE id = %s',
            ['confirmed', id]
            )
        