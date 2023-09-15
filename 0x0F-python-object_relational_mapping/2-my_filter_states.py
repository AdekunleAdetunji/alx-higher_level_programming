#!/usr/bin/python3

"""
This module is a python script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where name matches the argument
 provided via the command line
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    search_str = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=user, passwd=passwd,
                         port=3306, charset="utf8", db=dbname)

    query = """SELECT * FROM states """\
        """WHERE name LIKE '{}' """\
        """ORDER BY id;""".format(search_str)

    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
