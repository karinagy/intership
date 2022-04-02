from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels
from core.enums import Currency, StatusOfCar
from purchaser.models import Purchaser


class Car(AbstractDefaultModels):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    year = models.IntegerField(null=True)
    price = models.IntegerField(default=12000)
    currency = models.CharField(max_length=3,
                                choices=Currency.choices,
                                default=Currency.USD
                                )

    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            null=True
                            )
    status = models.CharField(max_length=255,
                              choices=StatusOfCar.choices,
                              default=StatusOfCar.Available
                              )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Rewiew(AbstractDefaultModels):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    car = models.ForeignKey(
        'car_dealership.Car',
        related_name='car_rewiew',
        on_delete=models.CASCADE
    )
    purchaser = models.ForeignKey(
        Purchaser,
        related_name='purchaser_rewiew',
        on_delete=models.PROTECT, null=True
    )

    def __str__(self):
        return self.name


class Raiting(models.Model):
    value = models.IntegerField(help_text='Рейтинг выставляется от 1 до 10')
    car = models.ForeignKey('car_dealership.Car', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.car)


class Car_dealership(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    characteristic = models.TextField(blank=True)
    location = CountryField(null=True)
    contact = models.EmailField()
    supplier = models.ManyToManyField(
        'supplier.Supplier',
        related_name='supplier_cardealer',
        null=True
    )
    car = models.ManyToManyField('car_dealership.Car')

    def __str__(self):
        return str(self.name)
