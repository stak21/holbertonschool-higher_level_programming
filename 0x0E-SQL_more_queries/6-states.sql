-- Creates a DB hbtn_0d_usa and table states
-- Description: id INT unique, auto generated, cant be null and is a primary key
-- ... name VARCHAR(256)
-- It should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
