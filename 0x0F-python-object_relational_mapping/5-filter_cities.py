#!/usr/bin/python3

"""
This module contains python script that list all the cities in the
hbtn_0e_4_usa database, with the output beign a table of join product of the
city table and the state table
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    user = sys.argv[1]
    passwd = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4].split(sep="'", maxsplit=1)[0]

    db = MySQLdb.connect(host="localhost", user=user, passwd=passwd,
                         port=3306, db=dbname, charset="utf8")

    query = """SELECT cities.name """\
        """FROM cities """\
        """INNER JOIN states ON states.id = cities.state_id """\
        """WHERE states.name = '{}' """\
        """ORDER BY cities.id""".format(state_name)
    cursor = db.cursor()
    cursor.execute(query)
    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))
