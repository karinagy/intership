from rest_framework import serializers

from car_dealership.models import *


class RaitinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raiting
        fields = ['car', 'value', 'time_create']
