#!/usr/bin/python3

"""
This a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":
    import sys
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
