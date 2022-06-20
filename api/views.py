from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django.db import models
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [ReadOnly]


class EditionViewSet(ModelViewSet):
    queryset = Edition.objects.all()
    serializer_class = Edition
    permission_classes = [ReadOnly]
