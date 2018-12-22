import uuid

import sqlalchemy

from app import db
from config import Config

import time
import datetime

def create_user(username, email, password):
    
    with db.engine.connect() as c:
        result = c.execute(sqlalchemy.text("""
            INSERT INTO "user_dawnletter" (
                username,
                email,
                hash_password,
                uuid
            )
            VALUES (
                :username,
                :email,
                :hash_password,
                :uuid
                )
            RETURNING id
        """), {
            "username": username,
            "email": email,
            "hash_password": password,
            "uuid": str(uuid.uuid4())
        })
        return result.fetchone()["id"]


USER_GET_COLUMNS = ['id', 'username', 'email', 'uuid', 'registered_on', 'confirmed']

def get_user(id):

    with db.engine.connect() as c:
        result = c.execute(sqlalchemy.text("""
            SELECT {columns}
              FROM "user_dawnletter"
             WHERE id = :id
        """.format(columns=','.join(USER_GET_COLUMNS))), {"id": id})
        row = result.fetchone()
        return dict(row) if row else None 
    
def get_user_by_email(email):

    with db.engine.connect() as c:
        result = c.execute(sqlalchemy.text("""
            SELECT {columns}
              FROM "user_dawnletter"
             WHERE email = :email
        """.format(columns=','.join(USER_GET_COLUMNS))), {"email": email})
        row = result.fetchone()
        return dict(row) if row else None 

def get_user_by_username(username):

    with db.engine.connect() as c:
        result = c.execute(sqlalchemy.text("""
            SELECT {columns}
              FROM "user_dawnletter"
             WHERE username = :username
        """.format(columns=','.join(USER_GET_COLUMNS))), {"username": username})
        row = result.fetchone()
        return dict(row) if row else None