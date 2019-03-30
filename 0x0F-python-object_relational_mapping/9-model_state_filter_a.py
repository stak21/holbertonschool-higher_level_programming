#!/usr/bin/python3
""" Script: lists all State objects that contain the letter """
from model_state import State, Base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        usr_name = sys.argv[1]
        usr_pass = sys.argv[2]
        usr_db = sys.argv[3]
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(usr_name, usr_pass, usr_db))
        Session = sessionmaker(bind=engine)

        session = Session()
        try:
            for state in session.query(State).\
                    filter(State.name.ilike('%a%')).\
                    all():
                        print("{}: {}".format(state.id, state.name))
        except:
            print("Nothing")
        session.close()
    else:
        print("my sql username pass db")
