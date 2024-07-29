import os
import unittest
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_chat_endpoint(self):
        print("Environment Variables:", os.environ)
        response = self.app.post(
            '/chat',
            json={
                'message': (
                    'What are some effective marketing strategies for a new '
                    'startup?'
                )
            }
        )
        print("Response:", response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.get_json())


if __name__ == '__main__':
    unittest.main()
