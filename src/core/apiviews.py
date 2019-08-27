from rest_framework import viewsets

from core.models import Client
from core.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    """A simple view to allow all CRUD operations"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
