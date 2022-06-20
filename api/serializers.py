from rest_framework.serializers import ModelSerializer, StringRelatedField
from django.contrib.auth.models import User
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class EditionSerializer(ModelSerializer):
    class Meta:
        model = Edition
        exclude = []


class GameSerializer(ModelSerializer):
    editions = EditionSerializer(many=True, read_only=True)
    genres = StringRelatedField(many=True)
    editor = StringRelatedField()
    developer = StringRelatedField()

    class Meta:
        model = Game
        fields = ["name", "release_date", "genres", "editor", "developer", "editions"]
