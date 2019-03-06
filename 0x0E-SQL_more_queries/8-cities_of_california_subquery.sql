-- Lists all the cities of CA that can be found in the DB hbtn_0d_usa
-- states contains record where name = California
-- Results ascd order by cities.id
-- no join
SELECT * FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
