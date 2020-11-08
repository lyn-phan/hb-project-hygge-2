from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(30))
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    password = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname}>'

class Trip(db.Model):
    """Built out trips are stored here. Will start with calendars/events to start as MVP"""

    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_name = db.Column(db.String(20))
    trip_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return f'<Trip trip_id={self.trip_id} trip_name={self.trip_name}>'

class User_trip(db.Model):
    """tracks which trips a user is a part of"""

    __tablename__ = 'user_trips'

    user_trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    trip = db.relationship('Trip', backref='user_trips')
    user = db.relationship('User', backref='user_trips')

    def __repr__(self):
        return f'<User_trip user_trip_id={self.user_trip_id}>'

class Event(db.Model):
    """track events on trip contributed by users"""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_name = db.Column(db.String(20))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    trip = db.relationship('Trip', backref='events')

    def __repr__(self):
        return f'<Event event_id={self.event_id} event_name={self.event_name}>'

#change ///ratings to project name?
# def connect_to_db(flask_app, db_uri='postgresql:///travel', echo=True):
def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///travel'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    """If the model is run or imported..."""
    from server import app
    connect_to_db(app)

    db.create_all()
    print('Connected to the database!')

