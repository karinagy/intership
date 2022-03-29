from django.db import models

from car_dealership.models import Cars
from core.models import AbstractDefaultModels


class Suplier(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    year_of_foundation = models.IntegerField()
    location = models.CharField(max_length=255)
    number_of_purchasers = models.IntegerField()
    about_company = models.TextField(blank=True)
    email_of_company = models.EmailField()
    founder = models.ForeignKey('Founder', on_delete=models.CASCADE, null=True)
    car = models.ManyToManyField(Cars)

    def __str__(self):
        return self.name


class Raiting(models.Model):
    value = models.IntegerField(help_text='Рейтинг выставляется от 1 до 10')
    suplier = models.ForeignKey('Suplier', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.suplier)


class Founder(AbstractDefaultModels):
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    pl_of_b = models.CharField(max_length=255, help_text='Страна, город', null=True)

    def __str__(self):
        return self.first_name
