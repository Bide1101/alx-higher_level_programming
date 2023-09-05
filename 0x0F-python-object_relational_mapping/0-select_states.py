#!/usr/bin/python3
""" This lists all states from a database """


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This access the datatbase and get the states from it.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db = db_connect.cursor()

    db.execute("SELECT * FROM states")

    rowSelect = db.fetchall()

    for row in rowSelected:
        print(row)
