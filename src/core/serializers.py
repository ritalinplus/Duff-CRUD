from rest_framework import serializers

from core.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """Basic serializer for Client model"""
    url = serializers.HyperlinkedIdentityField(
        view_name="clients-detail",
    )

    @staticmethod
    def _only_letters(value):
        """Allow only letters in value parameter.

        Args:
            value (str): data to check.

        Return:
            bool: True if string only has letters, False otherwise.

        """
        return value.isalpha()

    def validate_name(self, name):
        """Validates a person name.

        Args:
            name (str): name to check.

        Raise:
            ValidationError: if name not contains only letters.

        """
        if self._only_letters(name) is False:
            raise serializers.ValidationError("Only letters allowed")

    def validate_surname(self, surname):
        """Validates a person surname.

        Args:
            surname (str): surname to check.

        Raise:
            ValidationError: if surname not contains only letters.

        """
        if self._only_letters(surname) is False:
            raise serializers.ValidationError("Only letters allowed")

    class Meta:
        model = Client
        fields = '__all__'