from django.test import TestCase
from parameterized import parameterized
from rest_framework.serializers import ValidationError

from core.serializers import ClientSerializer


class TestCoreValidators(TestCase):

    @parameterized.expand([
        ("Homer", None),
        ("Milhouse", None),
        ("Comic Book Guy", None),
        ("Rick C 137", "Only letters and spaces allowed"),
        ("Squeaky-Voiced", "Only letters and spaces allowed"),
        ("    ", "Only letters and spaces allowed"),
    ])
    def test_validate_name(self, name, error_message):
        """Tests name validator

        Args:
            name (str): Client name.
            error_message (str): Expected error message.

        """
        try:
            validated_name = ClientSerializer.validate_name(name)
            self.assertEqual(validated_name, name)

        except ValidationError as e:
            self.assertEqual(e.args[0], error_message)

    @parameterized.expand([
        ("Simpson", None),
        ("Van Houten", None),
        ("Flanders", None),
        ("Ultrahouse 3000", "Only letters and spaces allowed"),
        ("Ralph-O-Cop", "Only letters and spaces allowed"),
        ("    ", "Only letters and spaces allowed"),
    ])
    def test_validate_surname(self, surname, error_message):
        """Tests surname validator.

        Args:
            surname (str): Client surname.
            error_message (str): Expected error message.

        """
        try:
            validated_surname = ClientSerializer.validate_surname(surname)
            self.assertEqual(validated_surname, surname)

        except ValidationError as e:
            self.assertEqual(e.args[0], error_message)

    @parameterized.expand([
        ("NL75ABNA6121940131", None),
        ("MT19ACDX65372895489962524836447", None),
        ("ES0720803551104745275693", None),
        ("GB89BARC20032661719162", None),
        ("GB89BARC20032661719163", "Invalid checksum digits"),
        ("SPR89BARC20032661719162", "Invalid characters in IBAN SPR89BARC20032661719162"),
        ("DX89BARC20032661719163", "Unknown country-code 'DX'"),
    ])
    def test_validate_iban(self, iban_account, error_message):
        """Tests IBAN account validator.

        Args:
            iban_account (str): Client IBAN account.
            error_message (str): Expected error message.

        """
        try:
            validated_iban = ClientSerializer.validate_iban(iban_account)
            self.assertEqual(validated_iban, iban_account)

        except ValidationError as e:
            self.assertEqual(str(e.args[0]), error_message)
