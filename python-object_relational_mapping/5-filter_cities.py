#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using db hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    # Verification of all required arguments
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password>\
              <database name> <state name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Command line args
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connection to MySQL Server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database
    )

    # Creating Cursor
    cursor = db.cursor()

    # Execute SQL Query
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Print result
    print(", ".join([row[0] for row in rows]))

    # Close cursor and database
    cursor.close()
    db.close
