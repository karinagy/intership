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
