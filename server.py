"""Server for Project Hygge app."""

from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db 
from crud import *

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "wanderlust"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ View Homepage """
    return render_template('homepage.html')

@app.route('/log_in', methods=["GET"])
def show_login():
    """show log in form"""

    return render_template('log_in.html')

@app.route('/log_in', methods=["POST"])
def process_login():
    """Logs user in site. Find user's login credentials located in
    'request.form' dictionary, look up user and store them in session"""

    existing_user = request.form.get('show_login')


@app.route('/calendar')
def calendar():
    """display calendars"""


@app.route('/trip')
def trip_summary():
    """display trip details"""

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True) 