from django.db import models


class Currency(models.TextChoices):
    EUR = 'EUR', 'EUR'
    USD = 'USD', 'USD'
    RUB = 'RUB', 'RUB'


class StatusOfCar(models.TextChoices):
    Available = 'Available'
    Out_of_stock = 'Out of stock'
    Withdrawn_from_sale = 'Withdrawn from sale'
