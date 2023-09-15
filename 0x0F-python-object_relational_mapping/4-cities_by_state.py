#!/usr/bin/python3

"""
This module contains python script that list all the cities in the
hbtn_0e_4_usa database, with the output beign a table of join product of
the city table and the state table
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=user, passwd=passwd,
                         port=3306, db=dbname, charset="utf8")

    query = """SELECT cities.id, cities.name, states.name """\
        """FROM cities """\
        """INNER JOIN states ON states.id = cities.state_id """\
        """ORDER BY cities.id"""
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
