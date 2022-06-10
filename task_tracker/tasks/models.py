from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Task(models.Model):
    """Модель задачи"""

    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание')
    date_to = models.DateField('Дата завершения задачи')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    performers = models.ManyToManyField(User, verbose_name='Исполнители', related_name='tasks')
    file = models.FileField('Документ', upload_to='tasks/', null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title
