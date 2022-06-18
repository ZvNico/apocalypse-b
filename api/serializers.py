from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        exclude = []


class EditionSerializer(ModelSerializer):
    class Meta:
        model = Edition
        exclude = []
