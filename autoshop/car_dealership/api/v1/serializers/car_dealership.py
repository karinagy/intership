from rest_framework import serializers

from car_dealership.models import *


class Car_dealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car_dealership
        fields = ['name', 'location', 'city', 'adress', 'contact', 'characteristic', 'time_create']
