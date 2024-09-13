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
    
    def all_by_id(self, user_id):
        rows = self._connection.execute('SELECT * from bookings WHERE user_id = %s ORDER BY id', [user_id])
        all_bookings = []
        for row in rows:
            item = Booking(row['id'], row['date_booked'], row['booking_status'], row['user_id'], row['space_id'])
            all_bookings.append(item)
        return all_bookings
    
    def get_booking(self, id):
        rows = self._connection.execute('SELECT * FROM bookings WHERE id = %s', [id])
        return rows[0]
    
    def create(self, booking):
        if self.is_date_unavailable(booking):
            raise Exception("This date is unavailable. Please choose another date.")
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
    
    def confirm_booking(self, id):
        rows = self._connection.execute(
            'UPDATE bookings SET booking_status = %s WHERE id = %s',
            ['confirmed', id]
            )

    def is_date_unavailable(self, booking):
        rows = self._connection.execute(
            'SELECT * FROM bookings \
                WHERE booking_status = %s AND space_id = %s',
                ['confirmed', booking.space_id]
                )
        unavailable_dates = [row['date_booked'] for row in rows]

        return booking.date_booked in unavailable_dates

        # def is_date_unavailable(self, booking):
        #     rows = self._connection.execute(
        #         # select specific date?
        #         'SELECT * FROM bookings \
        #             WHERE booking_status = %s AND space_id = %s',
        #             ['confirmed', booking.space_id]
        #             )
        #     unavailable_dates = [row['date_booked'] for row in rows]
        #     return booking.date_booked in unavailable_dates