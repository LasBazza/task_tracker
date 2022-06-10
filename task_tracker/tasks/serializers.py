import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Task

User = get_user_model()


class TaskSerializer(serializers.ModelSerializer):
    """Сериалайзер для работы с задачами"""

    performers = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        many=True,
    )
    date_to = serializers.DateField(
        format='%d.%m.%Y',
        input_formats=['%d.%m.%Y', 'iso-8601']
    )

    class Meta:
        model = Task
        fields = ('title', 'description', 'date_to', 'performers', 'file')

        extra_kwargs = {
            'file': {'required': False}
        }

    def create(self, validated_data):
        performers = validated_data.pop('performers')
        task = Task.objects.create(**validated_data)
        task.performers.set(performers)
        return task

    def validate_date_to(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError('Дата завершения не может быть в прошлом')
        return value

    def validate_performers(self, value):
        if not value:
            raise serializers.ValidationError('У задачи должен быть хотя бы один исполнитель')
        return value
