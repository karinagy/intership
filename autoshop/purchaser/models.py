from django.db import models

from core.models import AbstractDefaultModels


class Purchaser(AbstractDefaultModels):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.first_name
