#0x0F. Python - Object-relational mapping
---
## Description

This project in the low_level_programming series is about:

*Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))

*How to connect to a MySQL database from a Python script

*How to SELECT rows in a MySQL table from a Python script

*How to INSERT rows in a MySQL table from a Python script

*What ORM means

*How to map a Python Class to a MySQL table

---
File|Task
---|---
0-select_states.py | Script: Lists all states frmo the DB
1-filter_states.py | Script: lists all states with a name starting with N from the db
2-my_filter_states.py | Script: Displays all values int he states table where name matches the given arguments
3-my_safe_filter_states.py | Script: Displays all values in the states table of a db where name matches the argument, where it is safe from mysql injections
4-cities_by_state.py | Script: lists all cities fmor the DB
5-filter_cities.py | Script: Takes in the name of a state as argument and lists all cities of that state
model_state.py | Class: State - (Base Tips): Create a class called State
7-model_state_fetch_all.py | Script: Lists all State objects from the db
8-model_state_fetch_first.py | Script: prints the first State object form the db
9-model_state_filter_a.py | Script: lists all State objects that contain the letter a from the db
10-model_state_my_get.py | Script: Prints the State object with the name passed as argument
11-model_state_insert.py | Scirpt: Adds the State object "Louisiana" to the db
12-model_state_update_id_2.py | Script: Changes the name of a State object from the db
13-model_state_delete_a.py | Script: Deletes all State objects with a name containing the letter a
model_city.py | model_city.py

## Author
 Shoji Takashima
