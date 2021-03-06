from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер для регистрации новых пользователей"""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
