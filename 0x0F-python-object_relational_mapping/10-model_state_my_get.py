#!/usr/bin/python3

"""
This is a script that prints the first State object from the database
hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    state_name = sys.argv[4].split("'", 1)[0]
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).filter(State.name == state_name).first()
    if first_state:
        print("{}".format(first_state.id))
    else:
        print("Not found")

    session.close()
