#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states
from the `states` table where the name matches the given argument,
ordered by `id` in ascending order.
"""


import sys
import MySQLdb

# Make sure the script runs only if executed correctly
if __name__ == "__main__":
    # Verification of all required arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Command line args
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connection to MySQL Server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Creating Cursor
    cursor = db.cursor()

    # Execute the SQL query with format
    query = """
    SELECT * FROM states WHERE name LIKE BINARY'{}' ORDER BY states.id ASC
    """
    query = query.format(state_name)
    cursor.execute(query)

    # Fetch all the rows
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()

    # CLose the database
    db.close()
