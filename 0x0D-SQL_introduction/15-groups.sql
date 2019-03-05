-- List the number of records with the same score 
-- display the score and the number of the same score in descending order
SELECT score, COUNT(*) as number FROM `second_table` GROUP BY score ORDER BY score DESC;
