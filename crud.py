"""CRUD OPERATION"""

from model import db, User, Trip, User_trip, Event, connect_to_db
from datetime import datetime
from flask import Flask 

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

def add_user_session(user_id):
    """adds user to session"""

    all_trips = db.session.query(User.user_id, Trip.trip_name, User_trip.user_trip_id).join(User).all()

    user_id = session['user_id']
    current_user = User.query.get(session['user_id'])
    my_user_trip_id = current_user.user_trips
    my_user_trip_name = current_user.trips
    
    return my_user_trip_name

def create_new_trip(trip_name):
    """retrieves data from new_trip form and creates new trip and adds to database """
    
    # trip_name = request.form.get('trip_name')
    # session['user_id'] = user_id

    new_trip = Trip(trip_name=trip_name)
    db.session.add(new_trip)
    db.session.commit()

    new_id = new_trip.trip_id

    user_trip = User_trip(trip_id=new_id, user_id=session['user_id'])

    db.session.add(user_trip)
    db.session.commit()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)