from django.contrib.auth.models import User
from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Client


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
        self.assertEqual(Client.objects.get().name, 'troy')
        self.assertEqual(Client.objects.get().surname, 'mcclure')
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
        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'troy')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'mcclure')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)
        self.assertEqual(Client.objects.get(pk=client_2.pk).name, 'apu')
        self.assertEqual(Client.objects.get(pk=client_2.pk).surname, 'nahasapeemapetilon')
        self.assertEqual(Client.objects.get(pk=client_2.pk).iban, 'IT66G0300203280976671422723')
        self.assertEqual(Client.objects.get(pk=client_2.pk).owner, self.user)

    @tag('unit')
    def test_api_client_put(self):
        """Tests API PUT method"""
        user = User.objects.create(username="Santa's Little Helper")
        client_1 = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)
        client_2 = Client.objects.create(name='Ralph', surname='Wiggum', iban='LT266267441777929636', owner=user)

        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'troy')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'mcclure')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)

        self.assertEqual(Client.objects.get(pk=client_2.pk).name, 'ralph')
        self.assertEqual(Client.objects.get(pk=client_2.pk).surname, 'wiggum')
        self.assertEqual(Client.objects.get(pk=client_2.pk).iban, 'LT266267441777929636')
        self.assertEqual(Client.objects.get(pk=client_2.pk).owner, user)

        data = {
            'name': 'Apu',
            'surname': 'Nahasapeemapetilon',
            'iban': 'IT66G0300203280976671422723'
        }

        response = self.client.patch(self._create_pk_url(client_2.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.put(self._create_pk_url(client_1.pk), data, format='json')
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'apu')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'nahasapeemapetilon')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'IT66G0300203280976671422723')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)

    @tag('unit')
    def test_api_client_patch(self):
        """Tests API PATCH method"""
        user = User.objects.create(username="Santa's Little Helper")
        client_1 = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)
        client_2 = Client.objects.create(name='Ralph', surname='Wiggum', iban='LT266267441777929636', owner=user)

        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'troy')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'mcclure')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)

        self.assertEqual(Client.objects.get(pk=client_2.pk).name, 'ralph')
        self.assertEqual(Client.objects.get(pk=client_2.pk).surname, 'wiggum')
        self.assertEqual(Client.objects.get(pk=client_2.pk).iban, 'LT266267441777929636')
        self.assertEqual(Client.objects.get(pk=client_2.pk).owner, user)

        data = {
            'iban': 'IT66G0300203280976671422723'
        }

        response = self.client.patch(self._create_pk_url(client_2.pk), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.patch(self._create_pk_url(client_1.pk), data, format='json')
        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'troy')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'mcclure')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'IT66G0300203280976671422723')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)

    @tag('unit')
    def test_api_client_delete(self):
        """Tests API DELETE method"""
        user = User.objects.create(username="Santa's Little Helper")
        client_1 = Client.objects.create(name='Troy', surname='McClure', iban='LU950103192894472928', owner=self.user)
        client_2 = Client.objects.create(name='Ralph', surname='Wiggum', iban='LT266267441777929636', owner=user)

        self.assertEqual(Client.objects.count(), 2)
        self.assertEqual(Client.objects.get(pk=client_1.pk).name, 'troy')
        self.assertEqual(Client.objects.get(pk=client_1.pk).surname, 'mcclure')
        self.assertEqual(Client.objects.get(pk=client_1.pk).iban, 'LU950103192894472928')
        self.assertEqual(Client.objects.get(pk=client_1.pk).owner, self.user)
        self.assertEqual(Client.objects.get(pk=client_2.pk).name, 'ralph')
        self.assertEqual(Client.objects.get(pk=client_2.pk).surname, 'wiggum')
        self.assertEqual(Client.objects.get(pk=client_2.pk).iban, 'LT266267441777929636')
        self.assertEqual(Client.objects.get(pk=client_2.pk).owner, user)

        response = self.client.delete(self._create_pk_url(client_2.pk))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        response = self.client.delete(self._create_pk_url(client_1.pk))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 1)

    def _create_pk_url(self, pk):
        """Creates absolute url to get client object by primary key

        Args:
            pk (int): object primary key.

        Return:
            str: API endpoint, e.g. 4 -> /api/v1/clients/4/

        """
        return f'{self.url}{pk}/'
