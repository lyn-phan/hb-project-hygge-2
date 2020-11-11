"""Server for Project Hygge app."""

from flask import Flask, render_template, request, flash, session, redirect, flash
from model import User, Trip, User_trip, Event, connect_to_db, db
import jinja2
from crud import *

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "wanderlust"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ View Homepage """
    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def login():
    """Logs user in site. Find user's login credentials located in
    'request.form' dictionary, look up user and store them in session"""

    fname = request.form.get('fname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.authenticate(fname, email, password)

    if user:
        session['email'] = user.email
        session['fname'] = user.fname
        session['user_id'] = user.user_id
 
        return redirect('/home')
    else:
        flash("Sorry, we couldn't find your profile. Please log in or create an account.")
        return redirect('/')    

@app.route('/login', methods=['GET'])
def show_login():
    """show log in form"""

    return render_template('login.html')

@app.route('/signup', methods=['POST'])
def signup():
    """add a user to the database"""

    email = request.form.get('email')
    password = request.form.get('password')

    found_user = User.query.filter_by(email=email).all()

    if found_user:
        message = "Welcome back! Please log in."
    
    else:
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')

        user = User(fname=fname, lname=lname, email=email, password=password)

        db.session.add(user)
        db.session.commit()

        message = f'Thanks for signing up, {fname}! Please log in to get started.'
    
    flash(message)
    return redirect('/')

@app.route('/signup')
def show_signup():
    """displays signup page"""

    return render_template('signup.html')

@app.route('/home')
def show_home():
    """displays user's homepage once logged in. This
    includes trips that a user is a part of"""

    all_trips = db.session.query(User.user_id, Trip.trip_name, User_trip.user_trip_id).join(User).all()

    user_id = session['user_id']
    current_user = User.query.get(session['user_id'])
    my_user_trip_id = current_user.user_trips
    my_user_trip_name = current_user.trips
    
    return render_template('home.html', my_user_trip_name=my_user_trip_name)

@app.route('/trips/new')
def show_new_trip_form():
    """shows form to add a new trip. This form sends to
    /trips"""

    return render_template('new_trips.html')

@app.route('/trips/new', methods=['POST'] )
def show_new_trip():
    """retrieves data from new_trip form and creates new trip and adds to database """
    user_id = session['user_id']
    trip_name = request.form.get('trip_name')
    # trip_date = request.form.get('trip_date') #deal with datetime later

    new_trip = Trip(trip_name=trip_name)
    new_trip_id = Trip.query.filter(new_trip['trip_id'])
    create_trip = User_trip(trip_id=new_trip_id, user_id=session['user_id'])

    db.session.add(new_trip, create_trip)
    db.session.commit()

    return redirect('/home')

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True) 