from rest_framework import viewsets

from core.models import User
from core.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """A simple view to allow all CRUD operations"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
