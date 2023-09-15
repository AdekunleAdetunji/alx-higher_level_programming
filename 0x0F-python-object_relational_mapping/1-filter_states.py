#!/usr/bin/python3

"""
This module contains python code that lists all states from the hbtn_0e_0_usa
database
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user, port=3306,
                         passwd=passwd, db=dbname, charset="utf8")

    query = """SELECT * FROM states """\
        """WHERE name LIKE 'N%' """\
        """ORDER BY id"""
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
