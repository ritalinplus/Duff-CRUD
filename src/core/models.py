from django.db import models


class Member(models.Model):
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}'.format(self.description)

    class Meta:
        verbose_name_plural = "Categories"
