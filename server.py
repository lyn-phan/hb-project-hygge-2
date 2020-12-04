"""Server for Project Hygge app."""

from flask import Flask, render_template, request, flash, session, redirect, flash, jsonify
from model import User, Trip, User_trip, Event, connect_to_db, db
import crud 
import sqlalchemy

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "wanderlust"
app.jinja_env.undefined = StrictUndefined

######## NAVIGATION ##############
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

    user = crud.authenticate(fname, email, password)

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

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.create_user(fname=fname, lname=lname, email=email, password=password)

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

    joined_user_trips = db.session.query(User.user_id, Trip.trip_name, User_trip.user_trip_id).join(User).all()

    user_id = session['user_id']
    current_user = User.query.get(session['user_id'])
    my_user_trip_name = current_user.trips

    return render_template('home.html', my_user_trip_name=my_user_trip_name)

############### TRIPS ####################
@app.route('/trips/')
def show_all_trips():
    """shows a list of trips able to edit"""
    if 'email' in session:
        current_user = session['user_id']
        user_trip_id_list = crud.get_trip_id(session['user_id'])

    trip_objects_list =[]
    for tripId in user_trip_id_list:
        trip_objects = crud.get_trip_objects(tripId) # POPULATE THIS LIST WITH TRIP OBJECTS
        trip_objects_list.append(trip_objects)

    return render_template('trips.html', trip_objects_list=trip_objects_list)

@app.route('/trips/<trip_id>')
def show_each_trip_page(trip_id):
    """ shows each trip page from clicking on the name """
    destination = crud.get_trip_name(trip_id)
    trip_attendees = crud.return_attendees(trip_id)

    return render_template('trip_details.html', trip_id=trip_id, trip_attendees=trip_attendees, destination=destination)

# this function worked before jsonified function on line 123
# @app.route('/trips/<trip_id>', methods=['POST'])
# def add_friend_to_trip(trip_id):
#     """post request for adding a friend form"""
#     destination = crud.get_trip_name(trip_id)
#     new_email = request.form.get('email')
#     found_invite = crud.find_user(email=new_email)

#     if found_invite:
#         found_id = crud.get_user_id(email=new_email)
#         add_friend_to_trip = crud.create_user_trip(user_id=found_id, trip_id=trip_id)
#         flash(f"You and {found_invite} are going to {destination}!")
#     else:
#         flash("Sorry, your friend hasn't signed up yet.")
    
#     return redirect(f'/trips/{trip_id}') # return redirect('/trips/add-trip-event')

@app.route('/trips/<trip_id>', methods=['POST'])
def add_friend_jsonified(trip_id):
    """grabs data from trip details page and jsonifies it and adds to database"""

    friend_first = request.form.get('friendFirstName')
    friend_last = request.form.get('friendLastName')
    friend_email = request.form.get('friendEmail')

    data = {'friend_first': friend_first, 'friend_last': friend_last, 'friend_email': friend_email}

    found_invite = crud.find_user(email=new_email)

    if found_invite:
        found_id = crud.get_user_id(email=new_email)
        add_friend_to_trip = crud.create_user_trip(user_id=found_id, trip_id=trip_id)
    
    return jsonify(data)

@app.route('/trips/<trip_id>/add-trip-event', methods=['POST'])
def add_trip_event(trip_id):
    """grabs the data from addEventForm in trip_details.js file"""

    new_event_name = request.form.get('eventFormInput')
    new_event_date = request.form.get('eventDateInput')
    new_event_details = request.form.get('eventDescriptionInput')

    data = {'new_event_name': new_event_name, 'new_event_date': new_event_date, 'new_event_details': new_event_details}

    newEvent = crud.create_event(trip_id=trip_id, event_name=new_event_name, event_date=new_event_date, event_details=new_event_details)

    # return render_template('trip_details.html')
    return jsonify(data)

    # return redirect(f'/trips/{trip_id}')  # return redirect(f'/trips/{trip_id}', newEvent=newEvent)


##########################################################
@app.route('/trips/<trip_id>/event/new')
def show_event_details(trip_id):
    """shows the details of the events page"""
    destination = crud.get_trip_name(trip_id)

    return render_template('new_event.html', destination=destination, trip_id=trip_id)

@app.route('/trips/<trip_id>/event/new', methods=['POST'])
def create_new_event(trip_id):
    """shows a form to create a new event and adds it to trip_details page"""
    destination = crud.get_trip_name(trip_id)

    name_of_event = request.form.get('event_name')
    new_event_object = crud.create_event(trip_id=trip_id, event_name=name_of_event)

    if new_event_object:
        flash(f"You've added {name_of_event} to your trip to {destination}.")
    else:
        flash("Sorry, we couldn't add your trip. Please try again.")

    return redirect(f'/trips/{trip_id}/event/new')


@app.route('/trips/new')
def show_new_trip_form():
    """shows form to add a new trip. This form sends to /trips"""

    return render_template('new_trips.html')

@app.route('/trips/new', methods=['POST'] )
def show_new_trip():
    """retrieves data from new_trip form and creates new trip and adds to database """
    
    trip_name = request.form.get('trip_name')
    new_trip = crud.create_trip(trip_name=trip_name)

    new_id = new_trip.trip_id 
    user_trip = crud.create_user_trip(user_id=session['user_id'], trip_id=new_id)

    friends_email = request.form.get('email')
    found_user = User.query.filter_by(email=friends_email).all()

    if found_user:
        friend_id = found_user[0].user_id
        user_trip = crud.create_user_trip(user_id=friend_id, trip_id=new_id)
        flash("You're going places! You and your friends are going on a trip.")
    else:
        flash("Sorry, your friend hasn't signed up yet.")

    return redirect('/home')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True) 