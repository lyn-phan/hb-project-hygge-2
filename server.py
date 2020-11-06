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

@app.route('/login')
def login_page():
    """log in page"""

    return render_template('login.html')

@app.route('/calendar')
def calendar():
    """display calendars"""


@app.route('/trip')
def trip_summary():
    """display trip details"""

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True) 