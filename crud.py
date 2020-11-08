"""CRUD OPERATION"""

from model import db, User, Trip, connect_to_db
from datetime import datetime
from flask import Flask 

def create_user(fname, lname, password):
    """create and return a new user"""
    user = User(fname=fname, lname=lname, password=password)

    db.session.add(user)
    db.session.commit()

    return render_template("log_in.html")

def create_group(group_name, group_password):
    """create group and return new group"""
    group = Group(group_name=group_name, group_password=group_password)

    db.session.add(group)
    db.session.commit()

    return group

def create_trip(trip_name):
    """create and return new trip"""
    trip = Trip(trip_name=trip_name)

    db.session.add(trip)
    db.session.commit()

    return trip

if __name__ == '__main__':
    from server import app
    connect_to_db(app)