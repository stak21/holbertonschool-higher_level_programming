-- Creates the table unique_id
-- Description: id INT def_val 1 uniq, name VARCHAR(256)
-- It should not fail
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
