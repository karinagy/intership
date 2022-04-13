from car_dealership.models import Car_dealershipSelling
from rest_framework import serializers


class Car_dealershipSellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_dealershipSelling
        exclude = ['is_published']
