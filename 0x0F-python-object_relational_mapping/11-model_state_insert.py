#!/usr/bin/python3

"""
This module is a script that adds the State object “Louisiana” to the database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    louis = State(name="Louisiana")
    session.add(louis)
    session.commit()
    print(louis.id)
    session.close()
