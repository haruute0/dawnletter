from flask_testing import TestCase

from app import app, db
from app.models import User

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app