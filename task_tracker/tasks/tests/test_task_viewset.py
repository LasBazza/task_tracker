from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from tasks.models import Task

User = get_user_model()


class TestTaskViewSet(TestCase):
    """Класс тестирования работы с задачами"""

    def setUp(self) -> None:
        self.client_creator = APIClient()
        self.user_creator = User.objects.create_user(
            username='creator',
            full_name='Ivan Ivanov',
            password='password'
        )

        self.client_creator.force_authenticate(user=self.user_creator)

    def test_create_task(self):
        """Проверка создания задачи"""

        data = {
            'title': 'test_task',
            'description': 'create task',
            'date_to': '25.12.2022',
            'performers': [1]
        }

        self.client_creator.post('/api/tasks/', data)

        expected = Task.objects.filter(title='test_task', author__username='creator').exists()
        self.assertTrue(expected)

    def test_update_task(self):
        """Проверка редактирования задачи"""

        task = Task.objects.create(
            title='test_task',
            description='update task',
            date_to='2022-12-25',
            author=self.user_creator
        )

        data = {'description': 'task is updated'}

        self.client_creator.patch('/api/tasks/1/', data)
        task.refresh_from_db()

        self.assertEqual(task.description, 'task is updated')

    def test_edit_another_task(self):
        """Проверка запрета доступа к задаче, созданной другим пользователем"""

        another_user = User.objects.create_user(
            username='another',
            full_name='Petr Petrov',
            password='password'
        )
        another_client = APIClient()
        another_client.force_authenticate(user=another_user)

        Task.objects.create(
            title='test_task',
            description='edit task',
            date_to='2022-12-25',
            author=self.user_creator
        )

        data = {'description': 'breach of order'}

        response = another_client.patch('/api/tasks/1/', data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
