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
# def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
#     db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
#     repository = AlbumRepository(db_connection) # Create a new AlbumRepository 

#     albums = repository.all() # Get all albums

#     # Assert on the results
#     assert albums == [Album(1, 'Doolittle', 1989, 1), Album(2, 'Surfer Rosa', 1988, 1), Album(3, 'Waterloo', 1974, 2), Album(4, 'Super Trouper', 1980, 2), Album(5, 'Bossanova', 1990, 1), Album(6, 'Lover', 2019, 3), Album(7, 'Folklore', 2020, 3), Album(8, 'I Put a Spell on You', 1965, 4), Album(9, 'Baltimore', 1978, 4), Album(10, 'Here Comes the Sun', 1971, 4), Album(11, 'Fodder on My Wings', 1982, 4), Album(12, 'Ring Ring', 1973, 2)]

# """