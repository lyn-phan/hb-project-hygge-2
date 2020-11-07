from model import User, Group, Trip, connect_to_db, db
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

def seed_user_group_trip(db):
    user = User(fname = 'Lynda',
                lname = 'Phan',
                password = 'hello')
    
    group = Group(group_name = 'Pikachu',
                  group_password = "let us go")
    
    trip = Trip(trip_name = 'Hawaii')
    
    db.session.add(user)
    db.session.add(group)
    db.session.add(trip)
    db.session.commit()

    print(user)

seed_user_group_trip(db)