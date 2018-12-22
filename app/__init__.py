from flask import Flask
from config import Config
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Config)

manager = Manager(app)

from app import routes