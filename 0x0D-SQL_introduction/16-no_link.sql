-- List all records of a table
-- Don't list rows without a name value
-- Display the score and the name in descending order by score
SELECT score, name FROM `second_table` WHERE name IS NOT NULL ORDER BY score DESC;
