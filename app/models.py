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
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    uuid = db.Column(db.String(36), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)

    def __init__(self, username, email, confirmed, confirmed_on=None):
        self.username = username
        self.email = email
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on

    def __repr__(self):
        return '<User {}>'.format(self.username)   

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_uuid(self):
        self.uuid = str(uuid.uuid4())
    
    def get_time_stamp(self):
        self.registered_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    
    def get_confirmed(self):
        self.confirmed = True
        self.confirmed_on = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))