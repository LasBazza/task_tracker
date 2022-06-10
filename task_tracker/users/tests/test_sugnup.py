from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

User = get_user_model()


class TestUserSignUp(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_sign_up(self):
        """Проверка создания пользователя при регистрации"""
        data = {
            'username': 'test_user',
            'full_name': 'Test User',
            'password': 'test_password'
        }
        self.client.post('/api/auth/signup/', data)

        self.assertTrue(User.objects.filter(username='test_user').exists())


