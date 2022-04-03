from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app


class APITestCase(TestCase):
    def setUp(self):
        self.client = TestClient(web_app)

    def test_main_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):  # on bd fail
        user_data = {
            'user': {
                'email': 'test@mail.com',
                'password': 'testpass',
                'first_name': 'J',
                'last_name': 'D',
                'nick_name': 'JD'
            }
        }
        response = self.client.post('/user', json=user_data)
        self.assertEqual(response.status_code, 200)
