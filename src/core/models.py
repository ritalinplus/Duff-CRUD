from django.db import models


class Client(models.Model):
    """User model class"""
    name = models.CharField(max_length=100, help_text='User name')
    surname = models.CharField(max_length=100, help_text='User surname')
    iban = models.CharField(max_length=100, help_text='User IBAN')

    def __str__(self):
        return f'{self.name} {self.surname} {self.iban}'

    class Meta:
        verbose_name_plural = "Clients"
