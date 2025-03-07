#!/usr/bin/python3
"""
Script that list all cities from db hbtn_0e_4_usa
"""
import sys
import MySQLdb


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

    # Execute SQL Query
    cursor.execute("""
                   SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC
                """)

    # Fetch all rows
    rows = cursor.fetchall()

    # Print result
    for row in rows:
        print(row)

    # Close cursor and database
    cursor.close()
    db.close
