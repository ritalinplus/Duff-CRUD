from rest_framework import serializers

from core.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Basic serializer for User Model"""
    url = serializers.HyperlinkedIdentityField(
        view_name="users-detail",
    )

    class Meta:
        model = User
        fields = '__all__'
