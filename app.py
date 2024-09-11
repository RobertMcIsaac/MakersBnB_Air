import os
from flask import Flask, request, render_template, redirect
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


#------------------- SPACES ROUTES -------------------#

@app.route('/spaces')
def get_spaces():

    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    list_of_spaces = repository.all()

    return render_template('spaces.html', spaces=list_of_spaces)

#------------------- REGISTER ROUTES -------------------#

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
        return render_template("/register.html", error=error)



@app.route('/register_success')
def register_successful():
    return render_template('/register_success.html)')


#------------------- BOOKING ROUTES -------------------#

@app.route('/booking/<int:user_id>/<int:space_id>', methods=["GET"])
def get_booking_form(user_id, space_id):
    return render_template('booking_form.html', user_id = user_id, space_id = space_id)



@app.route('/post_booking/<int:user_id>/<int:space_id>', methods=["POST"])
def post_booking(user_id, space_id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    date = request.form['date_booked']
    booking = Booking(
        None,
        date,
        'pending',
        user_id,
        space_id
        )
    booking = repo.create(booking)
    return redirect(f'/booking_complete/{booking.id}')
    
    

@app.route('/booking_complete/<int:id>', methods=['GET'])
def get_booking(id):
    connection = get_flask_database_connection(app)
    repo = BookingRepository(connection)
    booking = repo.get_booking(id)
    return render_template('booking.html', booking = booking)



@app.route('/booking_confirmed/<int:booking_id>', methods=["PUT"])
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


