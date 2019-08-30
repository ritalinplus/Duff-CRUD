from django.conf import settings
from django.db import models


class OwnerModel(models.Model):
    """Owner model class"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Client(OwnerModel):
    """Client model class"""
    name = models.CharField(max_length=100, help_text='Client first name')
    surname = models.CharField(max_length=100, help_text='Client surname')
    iban = models.CharField(max_length=100, unique=True, help_text='Client IBAN account')

    def __str__(self):
        return f'{self.name} {self.surname} {self.iban}'

    def save(self, *args, **kwargs):
        """Saves client attributes converting to lowercase name and surname"""
        self.name = self.name.lower()
        self.surname = self.surname.lower()

        return super(Client, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Clients"
