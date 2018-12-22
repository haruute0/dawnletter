import unittest

from flask import current_app
from flask_testing import TestCase

from app.utils import BaseTestCase

from config import Config

from app import db
import app.db.user as user_db

class UserCreationTest(BaseTestCase):

    def test_create(self):
        userId = user_db.create_user('test_user', 'test_user@gmail.com', 'test_user')
        self.assertIsNotNone(user_db.get_user(userId))
    
    def test_get_user_by_email(self):
        userId = user_db.create_user('test_user1', 'test_user1@gmail.com', 'test_user1')
        user = user_db.get_user_by_email('test_user1@gmail.com')
        self.assertEqual(user['id'], userId)
    
    def test_get_user_by_username(self):
        userId = user_db.create_user('test_user2', 'test_user2@gmail.com', 'test_user2')
        user = user_db.get_user_by_username('test_user2')
        self.assertEqual(user['id'], userId)


if __name__ == '__main__':
    unittest.main()