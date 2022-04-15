from django.db import models
from django_countries.fields import CountryField

from core.abstract_models import AbstractDefaultModels, AbstractDelete
from core.enums.car_dealership_enums import Currency, StatusOfCar, Sale
from core.validators import check_raiting



class Car(AbstractDefaultModels, AbstractDelete):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    year = models.IntegerField(null=True)
    price = models.IntegerField(default=12000)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )

    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        null=True
    )
    status = models.CharField(
        max_length=255,
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


class Review(AbstractDefaultModels, AbstractDelete):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    car = models.ForeignKey(
        Car,
        verbose_name='машину',
        related_name='reviews',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.name


class Raiting(AbstractDefaultModels, AbstractDelete):
    value = models.IntegerField(validators=[check_raiting], default=1)
    car = models.ForeignKey(

        Car,
        on_delete=models.CASCADE,
        verbose_name='рейтинг',
        related_name='raiting'

    )

    def __str__(self):
        return str(self.car)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Car_dealership(AbstractDefaultModels, AbstractDelete):
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

    class Meta:
        verbose_name = 'Список автомобилей автосалона'
        verbose_name_plural = 'Список автомобилей автосалонoв'

    def __str__(self):
        return str(self.car)


class Car_dealershipSelling(AbstractDefaultModels, AbstractDelete):
    dealership = models.ForeignKey(Car_dealership, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.IntegerField()
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )
    sale = models.CharField(
        max_length=255,
        choices=Sale.choices,
        default=Sale.No_sale
    )

    class Meta:
        verbose_name = 'Продажа авто'
        verbose_name_plural = 'Продажа авто'

    def __str__(self):
        return str(self.car)


class Car_dealershipSeasonsales(AbstractDefaultModels, AbstractDelete):
    name_of_sale = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )
    car_dealership = models.ForeignKey(
        Car_dealership,
        on_delete=models.CASCADE
    )
    first_price = models.IntegerField()
    now_price = models.IntegerField()
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.USD
    )
    sale = models.CharField(
        max_length=255,
        choices=Sale.choices,
        default=Sale.No_sale
    )
    location_of_dealership = CountryField()
    start_time = models.DateField()
    end_time = models.DateField()

    class Meta:
        verbose_name = 'Сезонная скидка'
        verbose_name_plural = 'Сезонные скидки'

    def __str__(self):
        return str(self.car)
