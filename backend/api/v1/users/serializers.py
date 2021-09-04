"""
Модуль сериализации данных приложения users
"""

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from backend.apps.companies.models import Company
from backend.apps.users.models import User, Position, Skill, Language


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для создания и обновления
    записей о пользователи
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'patronymic',
                  'age', 'email', 'password', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True},
        }

    def create(self, validated_data: dict) -> User:
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для вывода списка пользоваетелей
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'patronymic',
                  'age', 'email', 'is_staff', 'is_active', 'date_joined',
                  'created_at', 'updated_at']


class UserRetrieveCompanySerializer(ModelSerializer):
    """
    Сериализация информации о компании для вывода в детальной информации
    о пользователе
    """

    class Meta:
        model = Company
        fields = ['id', 'name', ]


class UserRetrievePositionSerializer(ModelSerializer):
    """
    Сериализация информации о должности для вывода в детальной информации
    о пользователе
    """
    company = UserRetrieveCompanySerializer(read_only=True)

    class Meta:
        model = Position
        fields = ['position', 'company']


class UserRetrieveSkillSerializer(ModelSerializer):
    """
    Сериализация информации о навыках для вывода в детальной информации
    о пользователе
    """

    class Meta:
        model = Skill
        fields = ['skill', 'level']


class UserRetrieveLanguageSerializer(ModelSerializer):
    """
    Сериализация информации о языках для вывода в детальной информации
    о пользователе
    """

    class Meta:
        model = Language
        fields = ['language', 'level']


class UserRetrieveSerializer(serializers.ModelSerializer):
    """
    Сериализация данных для вывода польной
    информации о пользователе
    """
    user_companies = UserRetrievePositionSerializer(many=True, read_only=True)
    skills = UserRetrieveSkillSerializer(many=True, read_only=True)
    languages = UserRetrieveLanguageSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ['password', 'companies']