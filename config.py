import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = False