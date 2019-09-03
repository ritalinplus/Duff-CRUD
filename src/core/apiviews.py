from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Client
from core.permissions import IsOwner
from core.serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    # A simple view to allow all CRUD operations
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, IsOwner]
