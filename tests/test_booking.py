from lib.booking import Booking
import pytest
from datetime import date

"""
Test booking inits correctly with id, date_booked, booking_status, user_id, space_id
"""
def test_booking_initialises():
    booking = Booking(2, '2024-12-10', 'confirmed', 1, 3 )
    assert booking.id == 2
    assert booking.date_booked == '2024-12-10'
    assert booking.booking_status == 'confirmed'
    assert booking.user_id == 1
    assert booking.space_id == 3

"""
Test that two idential bookings are equal
"""
def test_booking_objects_are_equal():
    booking_1 = Booking(2, '2024-12-10', 'confirmed', 1, 3 )
    booking_2 = Booking(2, '2024-12-10', 'confirmed', 1, 3 )
    assert booking_1 == booking_2

"""
Test that booking returns correctly as a string
"""
def test_booking_returns_string_repr():
    booking = Booking(2, '2024-12-10', 'pending', 1, 3 )
    assert str(booking) == "Booking(2, 2024-12-10, pending, 1, 3)"

"""
booking_status is can only be pending or confirmed
"""
def test_date_booked_is_either_pending_or_confirmed():
    booking_1 = Booking(2, '2024-12-10', 'pending', 1, 3 )
    assert booking_1.booking_status == "pending"

    booking_2 = Booking(2, '2024-12-10', 'confirmed', 1, 3 )
    assert booking_2.booking_status == "confirmed"
    
    with pytest.raises(Exception) as error:
        booking_3 = Booking(2, '2024-12-10', 'incorrect', 1, 3 )
    error_message = str(error.value)
    assert error_message == "Incorrect value: please enter either 'pending' or 'confirmed'"


"""
date_booked is a datetime object
"""

# import datetime convert string to date time and then assert date time object when converted back into a string == string of date

