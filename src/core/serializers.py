from rest_framework import serializers
from core.models import User


class UserSerializer(serializers.ModelSerializer):
    """Basic serializer for User Model"""
    class Meta:
        model = User
        fields = '__all__'
