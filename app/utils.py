from flask_testing import TestCase

from app import app

from config import Config

from app import db

class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        db.initialize_db_conn(Config.SQLALCHEMY_TEST_DATABASE_URI)
        return app