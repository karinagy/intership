from rest_framework import serializers

from car_dealership.models import *


class RewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewiew
        fields = ['name', 'text', 'car', 'time_create']
