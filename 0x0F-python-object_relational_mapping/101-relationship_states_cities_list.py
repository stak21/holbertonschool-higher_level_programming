#!/usr/bin/python3
""" Script: Lists all State objects and corresponding City objects """
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
        for states, cities in session.query(State, City).\
        filter(State.id == City.id).\
        order_by(State.id, City.id).\
        all():
            print("{}: {}".format(states.id, states.name))
            for city in states.cities:
                print("    {}: {}".format(city.id, city.name))
                
                
                
            
        session.close()

    else:
        print("mysql User Passwd DB")
