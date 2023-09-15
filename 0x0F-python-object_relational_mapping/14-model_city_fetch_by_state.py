#!/usr/bin/python3

"""
This is a script that prints all the cities contained in the City object
from the database hbtn_0e_14_usa
"""

if __name__ == "__main__":
    import sys
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    que_obj = session.query(State, City)
    result = que_obj.filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
