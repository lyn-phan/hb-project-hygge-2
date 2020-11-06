from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
    autoincrement=True,
    primary_key=True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    password = db.Column(db.String(20))
    # group_name = db.Column(db.String(20))
    # group_password = db.Column(db.String(10))
    # trip_id = db.Column(db.Integer)
    # group_id = db.Column(db.Integer)

    # group = db.relationship('Group')
    # trip = db.relationship('Trip')

    def __repr__(self):
        return f'<User user_id={self.user_id} fname={self.fname} lname={self.lname}>'

class Group(db.Model):
    """Group of travelers"""

    __tablename__ = 'groups'

    group_id = db.Column(db.Integer,
    autoincrement=True,
    primary_key=True)
    group_name = db.Column(db.String(20))
    # removed foreign key(trips.group_name)
    group_password = db.Column(db.String(15))

    # user = db.relationship('User')
    # trip = db.relationship('Trip')
    
    def __repr__(self):
        return f'<Group group_id={self.group_id} group_name={self.group_name}>'


class Trip(db.Model):
    """Built out trips are stored here. Will start with calendars/events to start as MVP"""

    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_name = db.Column(db.String(20))
    trip_date = db.Column(db.DateTime)
    group_name = db.Column(db.String(15))
    
    # group = db.relationship('Group')
    # user = db.relationship('User')

    def __repr__(self):
        return f'<Trip trip_id={self.trip_id} trip_name={self.trip_name}>'
    

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

