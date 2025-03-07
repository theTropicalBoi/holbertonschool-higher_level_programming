#!/usr/bin/python3
"""
Prints State objects with name passed as args from db hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Verification of all required arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password>\
              <database name> <state name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connection to SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the first by name
    state = session.query(State).filter(State.name == state_name).first()

    # Print result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
