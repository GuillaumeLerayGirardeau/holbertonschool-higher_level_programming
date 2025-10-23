#!/usr/bin/python3

"""
Takes a name and displays all states corresponding to the name
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

    state_name_search = arguments[3]
    cursor = db_connection.cursor()

    try:
        states_num = cursor.execute(
            "SELECT id, name FROM states WHERE name = %s ORDER BY id",
            (state_name_search,)
        )
        while i < states_num:
            m = cursor.fetchone()
            print(m)
            i += 1
    except Exception as e:
        print("Error :", e)
        exit()

    cursor.close()
    db_connection.close()
