from rest_framework import serializers
from schwifty import IBAN

from core.libraries.stringutils import StringUtils
from core.models import Client


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """Basic serializer for Client model"""
    url = serializers.HyperlinkedIdentityField(
        view_name="clients-detail",
    )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    @staticmethod
    def validate_name(name):
        """Validates a person name.

        Args:
            name (str): name to check.

        Raise:
            ValidationError: if name not contains only letters.

        """
        if StringUtils.only_letters_and_blanks(name) is False:
            raise serializers.ValidationError("Only letters and spaces allowed")

        return name

    @staticmethod
    def validate_surname(surname):
        """Validates a person surname.

        Args:
            surname (str): surname to check.

        Raise:
            ValidationError: if surname not contains only letters.

        """
        if StringUtils.only_letters_and_blanks(surname) is False:
            raise serializers.ValidationError("Only letters and spaces allowed")

        return surname

    @staticmethod
    def validate_iban(iban):
        """Validates a IBAN account.

        Args:
            iban (str): iban account to check.

        Raise:
            ValidationError: if the IBAN has invalid checksum digits or a unknown country-code.

        """
        try:
            IBAN(iban)

        except ValueError as e:
            raise serializers.ValidationError(e)

        return iban

    class Meta:
        model = Client
        fields = '__all__'
