-- Creates a table id_not_null
-- Description: id INT def_val = 1, name VARCHAR(256)
-- Should not fail
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256));
