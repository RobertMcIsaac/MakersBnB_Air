import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')



# BOOKING ROUTES
@app.route('/booking/display/<int:user_id>/<int:space_id>', methods=["POST"])
def post_booking(user_id, space_id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    booking = Booking(
        None,
        request.form['date_booked'],
        'pending',
        user_id,
        space_id
        )
    booking = repo.create(booking)
    return render_template("booking.html", booking = booking)
    # return '', 200
    
    
@app.route('/booking_completed/<int:booking_id>', methods=["PUT"])
def put_booking(booking_id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    booking = repo.confirm_booking(booking_id)
    return '' , 200

# space needs to display available bookings (get) via user id
# user_id to find there spaces -> space_id to find available bookings -> for that space  

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
