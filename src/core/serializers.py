from rest_framework import serializers

from core.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """Basic serializer for User Model"""
    url = serializers.HyperlinkedIdentityField(
        view_name="clients-detail",
    )

    class Meta:
        model = Client
        fields = '__all__'
