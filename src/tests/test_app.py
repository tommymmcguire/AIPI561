import unittest
from src.app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_chat_endpoint(self):
        response = self.app.post(
            '/chat',
            json={
                'message': (
                    'What are some effective marketing strategies for a new '
                    'startup?'
                )
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.get_json())


if __name__ == '__main__':
    unittest.main()
