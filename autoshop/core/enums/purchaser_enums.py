from django.db import models


class SexOfPurchaser(models.TextChoices):
    Male = 'Male'
    Female = 'Female'
