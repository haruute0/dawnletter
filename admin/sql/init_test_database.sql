-- Initialize database with postgres user then chown it to dawnletter as app user.

CREATE USER test_dawnletter NOSUPERUSER NOCREATEDB;
CREATE DATABASE test_dawnletter WITH OWNER = test_dawnletter TEMPLATE template0 ENCODING = 'UNICODE';