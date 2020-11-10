"""Server for Project Hygge app."""

from flask import Flask, render_template, request, flash, session, redirect, flash
from model import User, Trip, User_trip, Event, connect_to_db, db
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

    user = User.authenticate(email, password)

    if user:
        session['email'] = user.email
        fname['fname'] = user.fname
 
        return redirect('/')
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

        message = 'Thanks for signing up, %s! Please log in to get started.' %(fname)
    
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
    trip_name = request.form.get('trip_name')
    trip_date = request.form.get('trip_date')
    user_trip_id = request.form.get('user_trip_id')

    return render_template('home.html')

@app.route('/trips/new', methods=["POST"])
def trip_summary():
    """shows form to add a new trip. This form sends to
    /trips"""

# @app.route('/trips')
# def show_my_trips():

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True) 