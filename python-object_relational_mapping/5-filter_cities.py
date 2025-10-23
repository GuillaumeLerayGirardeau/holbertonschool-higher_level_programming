#!/usr/bin/python3

"""
Takes in the name of a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":

    i = 0
    arguments = sys.argv[1:]

    if len(arguments) != 4:
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
    state_search = arguments[3]

    try:
        cursor.execute(
            "SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC", (state_search,)
        )
        m = cursor.fetchall()
        cities_list = []
        for i in m:
            cities_list.append(i[0])
        result = ", ".join(cities_list)

        print(result)

    except Exception as e:
        print("Error :", e)
        exit()

    cursor.close()
    db_connection.close()
