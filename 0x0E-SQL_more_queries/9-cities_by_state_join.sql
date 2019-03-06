-- List all cities contained in the dB hbtn_0d_usa
-- display cities.id - cities.name - states.name
-- Results ascd order by cities.id
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities JOIN states WHERE cities.state_id = states.id ORDER BY cities.id ASC;
