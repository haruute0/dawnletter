from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import uuid
import datetime
import time

class post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String())

    def __init__(self, post):
        self.post = post

    def __repr__(self):
        return '<id {}>'.format(self.id)

class User(UserMixin, db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    uuid = db.Column(db.String(36))
    registered_at = db.Column(db.DateTime)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.username)   

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_uuid(self):
        self.uuid = str(uuid.uuid4())
    
    def get_time_stamp(self):
        ts = time.time()
        self.registered_at = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))