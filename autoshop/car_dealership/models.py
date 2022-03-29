from django.db import models

from core.models import AbstractDefaultModels


class Cars(AbstractDefaultModels):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles')

    ]
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    year = models.IntegerField(null=True)
    price = models.IntegerField(default=12000)
    curenncy = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    cat = models.ForeignKey('Category',
                            on_delete=models.PROTECT,
                            null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Rewiew(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    car = models.ForeignKey('Cars',
                            on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Raiting(models.Model):
    value = models.IntegerField(help_text='Рейтинг выставляется от 1 до 10')
    car = models.ForeignKey('Cars', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.car)


class Car_dealership(AbstractDefaultModels):
    name = models.CharField(max_length=255)
    characteristic = models.TextField(blank=True)
    location = models.CharField(max_length=255, help_text='Введите страну, город')
    contact = models.EmailField()

    car = models.ManyToManyField('Cars')

    def __str__(self):
        return str(self.name)
