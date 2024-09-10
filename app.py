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
@app.route('/booking/<int:user_id>/<int:space_id>', methods=["POST"])
def post_booking(user_id, space_id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    booking = Booking(
        None,
        'pending',
        request.form['date_booked'],
        user_id,
        space_id
        )
    id = repo.create(booking)
    return redirect(f"/booking/{id}")


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
