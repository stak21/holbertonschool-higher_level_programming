#!/usr/bin/python3
""" Script: lists all State objects that contain the letter """
from model_state import State, Base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        usr_name = sys.argv[1]
        usr_pass = sys.argv[2]
        usr_db = sys.argv[3]
        usr_match = sys.argv[4]
        engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                               format(usr_name, usr_pass, usr_db))
        Session = sessionmaker(bind=engine)

        session = Session()
        try:
            for state in session.query(State).\
                    filter(State.name == usr_match).\
                    order_by(State.id).\
                    all():
                    print(state.name)
        except:
            print("Not found")
        session.close()
    else:
        print("my sql username pass db match")
