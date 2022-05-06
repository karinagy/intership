from rest_framework import serializers

from purchaser.models import *


class PurchaserSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Purchaser
        exclude = ['is_published']
