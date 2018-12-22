BEGIN;

CREATE TABLE "User" (
	id                  SERIAL
	username            VARCHAR(64) NOT NULL,
	email               VARCHAR(120) NOT NULL,
	hash_password		VARCHAR(128) NOT NULL,
	uuid                VARCHAR(36) NOT NULL,
	registered_on       TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
	confirmed           TIMESTAMP WITH TIME ZONE,
);

ALTER TABLE "user" ADD CONSTRAINT user_username UNIQUE (username);
ALTER TABLE "user" ADD CONSTRAINT user_email UNIQUE (email);

COMMIT;