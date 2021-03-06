from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(30), nullable = False)
    fname = db.Column(db.String(20), nullable = False)
    lname = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    trip = db.relationship('Trip', secondary='user_trips', backref='users')
    
    def __repr__(self):
        return f'<user_id={self.user_id} fname={self.fname} lname={self.lname}>'
    
    @classmethod
    def authenticate(cls, fname, email, password):
        try:
            return cls.query.filter_by(fname=fname, email=email, password=password).one()
        except NoResultFound:
            return None

    @classmethod
    def find_email(cls, email):
        try:
            found_user = cls.query.filter_by(email=email).one()
            return found_user

        except NoResultFound:
            return None
             
class Trip(db.Model):
    """Built out trips are stored here. Will start with calendars/events to start as MVP"""

    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_name = db.Column(db.String(20))
    trip_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    user = db.relationship('User', secondary='user_trips', backref='trips')

    def __repr__(self):
        return f'{self.trip_name}'

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
        return f'<User_trip user_id={self.user_id} trip_id={self.trip_id}>'

class Event(db.Model):
    """track events on trip contributed by users"""

    __tablename__ = 'events'

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_name = db.Column(db.String(20))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    event_date = db.Column(db.DateTime)
    event_details = db.Column(db.String(80))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    trip = db.relationship('Trip', backref='events')

    def __repr__(self):
        return f'<Event event_id={self.event_id} event_name={self.event_name}>'

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

