from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels, Raiting
from core.enums.car_dealership_enums import Currency, StatusOfCar
from purchaser.models import Purchaser


class Car(AbstractDefaultModels):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    year = models.IntegerField(null=True)
    price = models.IntegerField(default=12000)
    currency = models.CharField(
        max_length=3,
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

    class Meta:
        ordering = ['title']
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'


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

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Raiting(AbstractDefaultModels, Raiting):
    car = models.ForeignKey(

        'car_dealership.Car',
        on_delete=models.CASCADE,
        related_name='carraiting'
    )

    def __str__(self):
        return str(self.car)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Car_dealership(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    characteristic = models.TextField(blank=True)
    location = CountryField(null=True)
    city = models.CharField(max_length=255, null=True)
    adress = models.CharField(

        help_text='Улица с номером дома',
        max_length=255,
        null=True
    )
    contact = models.EmailField()
    cars = models.ManyToManyField(
        Car,
        through='car_dealership.Car_m2m_Dealer',
    )

    class Meta:
        verbose_name = 'Aвтосалон'
        verbose_name_plural = 'Aвтосалоны'

    def __str__(self):
        return str(self.name)


class Car_m2m_Dealer(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT, default='')
    autoshop = models.ForeignKey(Car_dealership, on_delete=models.PROTECT, default='')
    date_joined = models.DateField(auto_now_add=True, null=True)
