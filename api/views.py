from rest_framework.viewsets import ModelViewSet
from django.db import models
from django.contrib.auth.models import User
from .serializers import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()
    serializer_class = Edition
