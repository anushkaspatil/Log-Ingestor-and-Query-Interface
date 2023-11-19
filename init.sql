CREATE DATABASE IF NOT EXISTS log_ingestor_db;

CREATE USER IF NOT EXISTS 'anushka'@'localhost' IDENTIFIED BY 'anushka';

GRANT ALL PRIVILEGES ON *.* TO 'anushka'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;
