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

def authenticate(fname, email, password):
    user = User.authenticate(fname, email, password)

    return user

def find_user(email):
    find_the_user = User.query.filter_by(email=email).all()

    return find_the_user

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

    my_trip = Trip.query.filter_by(trip_id=trip_id).first()
    my_trip_name = my_trip.trip_name
    return my_trip_name

def get_user_id(email):

    my_user = User.query.filter_by(email=email).first()
    my_user_id = my_user.user_id
    
    return my_user_id    

def get_trip_id(user_id):
    """looks up trip_id of the user"""
    my_user_trip = User_trip.query.filter_by(user_id=user_id).all()
    
    trip_ids = []

    for user_trip_info in my_user_trip:
        my_trip_ids = user_trip_info.trip_id
        trip_ids.append(my_trip_ids)
    
    return trip_ids


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
# [<User_trip user_trip_id=1 trip_id=1>, <User_trip user_trip_id=3 trip_id=2>, <User_trip user_trip_id=5 trip_id=3>]
# animals = ["cat", "dog", "snake"]