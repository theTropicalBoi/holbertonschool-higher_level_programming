#!/usr/bin/python3
"""
Prints all City objects from db hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Retrieves all cities with states, order by cities.id
    cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id.asc())
        .all()
    )

    # Print result
    for city, state in cities:
        print("{}: ({}) {}".format(
            state.name,
            city.id,
            city.name))

    # Close session
    session.close()
