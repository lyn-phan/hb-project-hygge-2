"""CRUD OPERATION"""

from model import db, User, Trip, User_trip, Event, connect_to_db
from datetime import datetime
from flask import Flask, session

def create_user(fname, lname, email, password):
    """create and return a new user"""
    user = User(fname=fname, lname=lname, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_trip(trip_name):
    """create and return new trip"""
    trip = Trip(trip_name=trip_name)

    db.session.add(trip)
    db.session.commit()

    return trip

def create_user_trip(user_id, trip_id):
    """create and return trips associated to a user"""
    user_trip = User_trip(user_id=user_id, trip_id=trip_id)

    db.session.add(user_trip)
    db.session.commit()

    return user_trip

def get_trip_name(trip_id):
    """Looks up trip_name by trip_id"""

    my_trip_name = Trip.query.filter_by(trip_id=trip_id).first()

    return my_trip_name

def get_user_id(user_):
    my_user_id = db.session.query(User.user_id).first()

    return my_user_id

def get_trip_id():
    """looks up trip_id



# def adds_user_in_session():
#     """ adds user_id in a session, and assigns user_trips to the current user """
    
#     joined_user_trips = db.session.query(User.user_id, Trip.trip_name, User_trip.user_trip_id).join(User).all()
# # joins User, Trip and User_trip tables
#     user_id = session['user_id']
#     # assigns user_id to the session
#     current_user = User.query.get(session['user_id'])
#     # looks up the the current user in session and assigns it to current_user

#     # my_user_trip_name = current_user.trips

    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)