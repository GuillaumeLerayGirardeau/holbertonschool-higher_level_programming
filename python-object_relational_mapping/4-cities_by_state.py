#!/usr/bin/python3

"""
Lists all cities from the database hbtn_0e_4_usa
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

    try:
        cursor.execute(
            "SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY id ASC"
        )
        m = cursor.fetchall()
        for i in m:
            print(i)

    except Exception as e:
        print("Error :", e)
        exit()

    cursor.close()
    db_connection.close()
