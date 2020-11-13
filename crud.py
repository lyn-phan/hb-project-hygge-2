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

def convert_tripid_name(trip_id):
    """Looks up trip_name by trip_id"""

    my_trip_name = Trip.query.filter_by(trip_id=trip_id).first()
    return my_trip_name
    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)