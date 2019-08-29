from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Client


from rest_framework.test import force_authenticate
from django.contrib.auth.models import User

class TestCoreApi(APITestCase):
    """Unit tests for core API."""
    def setUp(self):
        # Setup run before every test method.
        self.url = reverse('clients-list')
        self.user = User.objects.create(username='snowball')
        self.client.force_authenticate(self.user)

    @tag('unit')
    def test_api_client_post(self):
        """Tests API POST method"""
        data = {
            'name': 'Troy',
            'surname': 'McClure',
            'iban': 'LU950103192894472928'
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'Troy')
        self.assertEqual(Client.objects.get().surname, 'McClure')
        self.assertEqual(Client.objects.get().iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get().owner, self.user)

    @tag('unit')
    def test_api_client_get(self):
        """Tests API GET method"""
        client_1 = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)
        client_2 = Client.objects.create(
            name='Apu', surname='Nahasapeemapetilon', iban='IT66G0300203280976671422723', owner=self.user)

        response = self.client.get(self.url)

        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'Troy')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'McClure')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)

        self.assertEqual(Client.objects.get(pk=client_2.pk).name, 'Apu')
        self.assertEqual(Client.objects.get(pk=client_2.pk).surname, 'Nahasapeemapetilon')
        self.assertEqual(Client.objects.get(pk=client_2.pk).iban, 'IT66G0300203280976671422723')
        self.assertEqual(Client.objects.get(pk=client_2.pk).owner, self.user)

    @tag('unit')
    def test_api_client_put(self):
        """Tests API PUT method"""
        client = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)
        self.assertEqual(Client.objects.get(pk=client.pk).name, 'Troy')
        self.assertEqual(Client.objects.get(pk=client.pk).surname, 'McClure')
        self.assertEqual(Client.objects.get(pk=client.pk).iban, 'LU950103192894472928')

        data = {
            'name': 'Apu',
            'surname': 'Nahasapeemapetilon',
            'iban': 'IT66G0300203280976671422723'
        }

        response = self.client.put(self._create_pk_url(client.pk), data, format='json')

        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.get(pk=client.pk).name, 'Apu')
        self.assertEqual(Client.objects.get(pk=client.pk).surname, 'Nahasapeemapetilon')
        self.assertEqual(Client.objects.get(pk=client.pk).iban, 'IT66G0300203280976671422723')
        self.assertEqual(Client.objects.get(pk=client.pk).owner, self.user)

    @tag('unit')
    def test_api_client_patch(self):
        """Tests API PATCH method"""
        client = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)
        self.assertEqual(Client.objects.get(pk=client.pk).iban, 'LU950103192894472928')

        data = {
            'iban': 'IT66G0300203280976671422723'
        }

        response = self.client.patch(self._create_pk_url(client.pk), data, format='json')

        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.get(pk=client.pk).name, 'Troy')
        self.assertEqual(Client.objects.get(pk=client.pk).surname, 'McClure')
        self.assertEqual(Client.objects.get(pk=client.pk).iban, 'IT66G0300203280976671422723')
        self.assertEqual(Client.objects.get(pk=client.pk).owner, self.user)

    @tag('unit')
    def test_api_client_delete(self):
        """Tests API DELETE method"""
        client = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)

        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get(pk=client.pk).name, 'Troy')
        self.assertEqual(Client.objects.get(pk=client.pk).surname, 'McClure')
        self.assertEqual(Client.objects.get(pk=client.pk).iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get(pk=client.pk).owner, self.user)
        
        response = self.client.delete(self._create_pk_url(client.pk))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)

    def _create_pk_url(self, pk):
        """Creates absolute url to get client object by primary key

        Args:
            pk (int): object primary key.

        Return:
            str: API endpoint, e.g. 4 -> /api/v1/clients/4/

        """
        return f'{self.url}{pk}/'
