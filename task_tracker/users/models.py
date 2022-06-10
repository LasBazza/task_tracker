from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class User(AbstractUser):
    """Модель пользователя"""

    full_name = CharField('Полное имя', max_length=200)

    REQUIRED_FIELDS = ['full_name']

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
