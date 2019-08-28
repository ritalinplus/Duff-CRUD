from django.db import models


class Client(models.Model):
    """Client model class"""
    name = models.CharField(max_length=100, help_text='Client first name')
    surname = models.CharField(max_length=100, help_text='Client surname')
    iban = models.CharField(max_length=100, help_text='Client IBAN account')

    def __str__(self):
        return f'{self.name} {self.surname} {self.iban}'

    class Meta:
        verbose_name_plural = "Clients"
