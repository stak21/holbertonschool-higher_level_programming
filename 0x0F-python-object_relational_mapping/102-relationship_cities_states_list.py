#!/usr/bin/python3
""" Script: Lists all City objects """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base

if __name__ == "__main__":
    if len(sys.argv) == 4:
        usr_name = sys.argv[1]
        usr_passwd = sys.argv[2]
        usr_db = sys.argv[3]

        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(usr_name, usr_passwd, usr_db))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)

        session = Session()
        for cities in session.query(City).\
                order_by(City.id).\
                all():
                    print("{}: {} -> {}".format(
                        cities.id, cities.name, cities.state.name))
        session.close()

    else:
        print("mysql USER PASSWD DB")
