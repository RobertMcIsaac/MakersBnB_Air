from lib.booking_repository import BookingRepository 
from lib.booking import Booking
from datetime import date

def test_read_bookings(db_connection):
    db_connection.seed('seeds/air_makersbnb_test.sql')
    bookings = BookingRepository(db_connection)
    all_bookings = bookings.all()
    
    for booking in all_bookings:
        print(f'Booking({booking.id}, {booking.date_booked}, {booking.booking_status}, {booking.user_id}, {booking.space_id}),')

    
    assert all_bookings == [Booking(1, date(2024,9,25), 'confirmed', 1, 3), Booking(2, date(2024,11,23), 'confirmed', 1, 5), Booking(3, date(2025,9,20), 'pending', 2, 1), Booking(4, date(2024,10,15), 'pending', 2, 4), Booking(5, date(2024,12,30), 'pending', 1, 2)]

def test_create_booking(db_connection):
    db_connection.seed('seeds/air_makersbnb_test.sql')
    bookings = BookingRepository(db_connection)
    new_booking = bookings.create(Booking(None, date(2024,9,25), 'confirmed', 1, 3))
    
    assert bookings.all() == [Booking(1, date(2024,9,25), 'confirmed', 1, 3), Booking(2, date(2024,11,23), 'confirmed', 1, 5), Booking(3, date(2025,9,20), 'pending', 2, 1), Booking(4, date(2024,10,15), 'pending', 2, 4), Booking(5, date(2024,12,30), 'pending', 1, 2), Booking(6, date(2024,9,25), 'confirmed', 1, 3)]
        
def test_update_booking(db_connection):
    db_connection.seed('seeds/air_makersbnb_test.sql')
    new = BookingRepository(db_connection)
    new.confirm_booking(3) 
    # bookings = BookingRepository(db_connection)
    
    assert new.all() == [Booking(1, date(2024,9,25), 'confirmed', 1, 3), Booking(2, date(2024,11,23), 'confirmed', 1, 5), Booking(3, date(2025,9,20), 'confirmed', 2, 1), Booking(4, date(2024,10,15), 'pending', 2, 4), Booking(5, date(2024,12,30), 'pending', 1, 2)]
