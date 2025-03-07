#!/usr/bin/python3
"""
Changes the name of a State object from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Verification of all required arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connection to SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(username, password, database),
        pool_pre_ping=True
    )

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State id 2 and modify to "New Mexico"
    state_to_upd = session.query(State).filter(State.id == 2).first()
    if state_to_upd:
        state_to_upd.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
