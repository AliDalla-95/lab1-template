-- file: 10-create-user-and-db.sql
CREATE DATABASE distlab;
CREATE ROLE program WITH PASSWORD 'test';
GRANT ALL PRIVILEGES ON DATABASE distlab TO program;
ALTER ROLE program WITH LOGIN;