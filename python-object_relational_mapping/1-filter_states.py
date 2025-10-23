#!/usr/bin/python3

"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":

    i = 0
    arguments = sys.argv[1:]

    if len(arguments) != 3:
        print("Invalid number of arguments !")
        exit()

    try:
        db_connection = MySQLdb.connect(
            host="localhost",
            user=arguments[0],
            password=arguments[1],
            db=arguments[2],
            port=3306
        )
    except Exception as e:
        print("Can't connect to the database :", e)
        exit()

    cursor = db_connection.cursor()
    states_num = cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id"
    )
    while i < states_num:
        m = cursor.fetchone()
        print(m)
        i += 1

    cursor.close()
    db_connection.close()
