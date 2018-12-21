import unittest

from flask_login import current_user

from app.util import BaseTestCase


class TestPublic(BaseTestCase):

    def test_main_route_requires_login(self):
        # Ensure main route requres logged in user.
        response = self.client.get('/', follow_redirects=True)
        self.assertTrue(response.status_code == 200)
        self.assertIn(b'Please log in to access this page', response.data)

    def test_logout_route_requires_login(self):
        # Ensure logout route requres logged in user.
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)


class TestLoggingInOut(BaseTestCase):

    def test_correct_login(self):
        # Ensure login behaves correctly with correct credentials
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            self.assertIn(b'Welcome', response.data)
            self.assertTrue(current_user.email == "admin@admin.com")
            self.assertTrue(response.status_code == 200)

    def test_logout_behaves_correctly(self):
        # Ensure logout behaves correctly, regarding the session
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="admin", password="admin"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'Please log in to access this page', response.data)


if __name__ == '__main__':
    unittest.main()