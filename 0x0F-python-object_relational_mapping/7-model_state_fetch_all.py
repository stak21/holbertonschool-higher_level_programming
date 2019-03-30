#!/usr/bin/python3
""" Script: lists all State objects from the db """
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

        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
        session.close()
    else:
        print("my sql username pass db")
