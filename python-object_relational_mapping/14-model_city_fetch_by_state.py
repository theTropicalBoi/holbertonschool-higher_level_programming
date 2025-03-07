#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_14_usa,
sorted by cities.id and showing their associated state names.
"""

import sys  # Import sys to handle command-line arguments
from model_city import Base, City  # Import the City and Base classes
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Ensure the script is provided with the correct arguments
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database),
        pool_pre_ping=True)  # Use pool_pre_ping to avoid connection issues

    # Create a session factory bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()  # Create session instance to interact with database

    # Query the City table, join with the State table, order by city.id
    cities = session.query(City).join(City.state).order_by(City.id).all()

    # Loop through the retrieved cities and print them along with their state
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    # Close the session to release resources
    session.close()
