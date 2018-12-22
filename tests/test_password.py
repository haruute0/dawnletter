import unittest

from flask import current_app
from flask_testing import TestCase

from app import models
from app.utils import BaseTestCase

class TestLogin(BaseTestCase):

    import app.models.login as login

    def test_hash(self):
        hashed_password = self.login.generate_hashed_password('test_password')
        password_correct = self.login.check_password('test_password', hashed_password)
        self.assertTrue(password_correct)

if __name__ == '__main__':
    unittest.main()