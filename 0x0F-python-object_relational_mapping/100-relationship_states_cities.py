#!/usr/bin/python3
""" Script: Creates the State "California" with the City "San Francisco """
import sys
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) == 4:
        usr_name = sys.argv[1]
        usr_pass = sys.argv[2]
        usr_db = sys.argv[3]
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(usr_name, usr_pass, usr_db))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        session = Session()
        state = State(name="California")
        state.cities = [City(name="San Francisco")]
        session.add(state)
        session.commit()

        session.close()
    else:
        print("mysql User Passwd DB")
