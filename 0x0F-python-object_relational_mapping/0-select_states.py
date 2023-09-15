#!/usr/bin/python3

"""
This module contains python code that lists all states from the database
hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=dbname, charset="utf8")

    query = """SELECT * FROM states ORDER BY id"""

    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
