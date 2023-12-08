from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import Dog



def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    # Use .first() to get the first result or .all() to get all results
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    # Use .first() to get the first result or .all() to get all results
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    # Use multiple filter conditions to compare each attribute
    return session.query(Dog).filter(Dog.name == name, Dog.breed ==  breed).first()

def update_breed(session, dog, breed):
    # Update the breed attribute of the Dog instance
    dog.breed = breed
    
    # Commit the changes to the database
    session.commit()