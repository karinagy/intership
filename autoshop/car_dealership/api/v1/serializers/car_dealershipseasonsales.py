from car_dealership.models import Car_dealershipSeasonsales
from rest_framework import serializers


class Car_dealershipSeasonsalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_dealershipSeasonsales
        exclude = ['is_published']
