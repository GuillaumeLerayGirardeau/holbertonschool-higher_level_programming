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
    sql_query = ("SELECT id, name FROM states \
                 WHERE BINARY name = '{0}' ORDER BY id"
                 .format(state_name_search,))

    cursor = db_connection.cursor()

    try:
        cursor.execute(
            sql_query
        )
        m = cursor.fetchall()
        for i in m:
            print(i)

    except Exception as e:
        print("Error :", e)
        exit()

    cursor.close()
    db_connection.close()
