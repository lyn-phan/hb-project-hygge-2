from model import User, Trip, User_trip, Event, connect_to_db, db
import os
import crud
import server 


os.system('dropdb travel')
os.system('createdb travel')

connect_to_db(server.app)
db.create_all()

def get_users(db):
    return db.session.execute("""
        SELECT user_id, fname, lname
          FROM users
    """).fetchall()

def seed_user_trip(db):
    user = User(fname = 'Lynda',
                lname = 'Phan',
                email = 'lynda@lynda.com',
                password = 'hello')
    
    trip = Trip(trip_name = 'Hawaii')

    user_trip = User_trip(trip_id = 1,
                          user_id = 1)

    event = Event(event_id = 1,
                 trip_id = 1,
                 event_name = 'Summer 2020',
                  event_date = '2020-12-01')
    
    db.session.add(user)
    db.session.add(trip)
    db.session.add(user_trip)
    db.session.add(event)
    db.session.commit()

    return user

seed_user_trip(db)