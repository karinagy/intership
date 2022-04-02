from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels
from core.validators import check_year_of_foundation


class Supplier(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    year_of_foundation = models.IntegerField(validators=[check_year_of_foundation])
    location = CountryField()
    number_of_purchasers = models.IntegerField()
    about_company = models.TextField(blank=True)
    email_of_company = models.EmailField()
    founder = models.ForeignKey(
        'Founder',
        on_delete=models.CASCADE,
        null=True
    )
    autoshops = models.ManyToManyField(
        'car_dealership.Car_dealership',
        related_name='cardealer_supplier'
    )

    def __str__(self):
        return self.name


class Raiting(models.Model):
    value = models.IntegerField(help_text='Рейтинг выставляется от 1 до 10')
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.supplier)


class Founder(AbstractDefaultModels):
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    place_of_birth = CountryField(null=True)

    def __str__(self):
        return self.first_name
