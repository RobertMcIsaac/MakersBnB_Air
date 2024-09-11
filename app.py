import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.booking_repository import BookingRepository
from lib.booking import Booking
from lib.space_repository import SpaceRepository
from lib.user import User
from lib.user_repository import UserRepository

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
        request.form['date_booked'],
        'pending',
        user_id,
        space_id
        )
    booking = repo.create(booking)
    return render_template("booking.html", booking = booking)
    # return '', 200


# SPACES MAIN PAGE
@app.route('/spaces')
def get_spaces():

    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    list_of_spaces = repository.all()

    return render_template('spaces.html', spaces=list_of_spaces)

@app.route('/register')
def get_register_page():
    return render_template('/register.html')

@app.route('/register', methods=["POST"])
def register_user():
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    user = User(None, username, email, password)

    try:
        repository.create_user(user)
        return render_template("/register_success.html")
    
    except Exception as e:
        error = str(e)
        return render_template("/error.html", error=e)



@app.route('/register_success')
def register_successful():
    return render_template('/register_success.html)')













# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))


