from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_active']
        read_only_field = ['is_active', 'created', 'updated']


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = UserSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_active']

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user


class KeySerializer(ModelSerializer):
    class Meta:
        model = Key
        fields = ["id"]


class EditionSerializer(ModelSerializer):
    keys = KeySerializer(many=True, read_only=True)
    support = StringRelatedField()
    platform = StringRelatedField()

    class Meta:
        model = Edition
        fields = ["name", "isDLC", "price", "initial_price", "cover", "content", "platform", "support", "keys"]


class GameSerializer(ModelSerializer):
    editions = EditionSerializer(many=True, read_only=True)
    genres = StringRelatedField(many=True)
    editor = StringRelatedField()
    developer = StringRelatedField()
    default_edition = EditionSerializer(read_only=True)
    class Meta:
        model = Game
        fields = ["id", "name", "release_date", "description", "genres", "editor", "developer", "editions",
                  "default_edition"]
