import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):

    # Dir

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    COV_DIR = os.path.join(BASE_DIR, 'tmp/coverage')

    # PostgreSQL

    SQLALCHEMY_DATABASE_URI = "postgres://dawnletter:dawnletter@localhost/dawnletter"

    SQLALCHEMY_TEST_DATABASE_URI = "postgres://test_dawnletter:test_dawnletter@localhost/test_dawnletter"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTGRES_ADMIN_URI = os.environ.get('TRAVIS_POSTGRES_ADMIN_URI', "postgresql://postgres:postgres@localhost/postgres")

    ADMIN_SQL_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'admin', 'sql')

    # Flask-WTF

    SECRET_KEY = os.environ.get('SECRET_KEY', None)

    # Email confirmation config

    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', None)
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'from@example.com')

    # mail settings
    
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', None)

class TestingConfig(Config):
    
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
