"""Server for Project Hygge app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db 
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "wanderlust"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ View Homepage """
    return render_template('homepage.html')

@app.route('/login', methods=['GET'])
def show_login():
    """show log in form"""

    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """Logs user in site. Find user's login credentials located in
    'request.form' dictionary, look up user and store them in session"""
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    if user:
        session['fname'] = User.fname
        session['lname'] = User.lname
        return redirect['/']

@app.route('/signup', methods=['GET'])
def show_signup():
    """displays signup page"""

    return render_template('signup.html')

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

        user = User(fname=fname,
        lname=lname,
        email=email,
        password=password)

        db.session.add(user)
        db.session.commit()

        message = 'Thanks for signing up, %s! Please log in to get started.' %(fname)
    
    flash(message)
    return redirect('/login')

@app.route('/calendar')
def calendar():
    """display calendars"""


@app.route('/trip')
def trip_summary():
    """display trip details"""

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True) 