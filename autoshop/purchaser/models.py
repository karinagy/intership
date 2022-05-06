from django.db import models

from core.abstract_models import AbstractDefaultModels
from core.enums.purchaser_enums import SexOfPurchaser
from core.validators import check_phonenum


class Purchaser(AbstractDefaultModels):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    sex = models.CharField(

        max_length=6,
        choices=SexOfPurchaser.choices,
        default=SexOfPurchaser.Male

    )
    age = models.IntegerField()
    birth = models.DateField(null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(

        max_length=13,
        null=True,
        validators=[check_phonenum]
    )

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Balance(models.Model):
    value = models.IntegerField()
    purchaser = models.ForeignKey(
        Purchaser,
        on_delete=models.CASCADE,
        default=1000
    )

    def __str__(self):
        return str(self.purchaser)

    class Meta:
        ordering = ['value']
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
