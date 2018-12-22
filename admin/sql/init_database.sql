-- Initialize database with postgres user then chown it to dawnletter as app user.

CREATE USER dawnletter NOSUPERUSER NOCREATEDB;
CREATE DATABASE dawnletter WITH OWNER = dawnletter TEMPLATE template0 ENCODING = 'UNICODE';