import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):

    # PostgreSQL

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-WTF

    SECRET_KEY = os.environ.get('SECRET_KEY', None)

    # Email confirmation config

    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', None)
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'from@example.com')

    # mail settings
    
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', None)
