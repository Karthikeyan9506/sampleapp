# tests/test_app.py

from app import app
import unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_hello_endpoint(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Hello, CI/CD!')

if __name__ == '__main__':
    unittest.main()
