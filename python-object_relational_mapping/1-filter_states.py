#!/usr/bin/python3
"""
Script that lists all states with name
starting with N from hbtn_0e_0_usa
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

    # Execute SQL Query to filter states beginning with N
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Print result
    for row in rows:
        if row[1].startswith("N"):
            print(row)

    # Close cursor and database
    cursor.close()
    db.close
