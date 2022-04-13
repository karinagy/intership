from car_dealership.models import Car
from rest_framework import serializers

from car_dealership.api.v1.serializers.raiting import RaitinSerializer
from car_dealership.api.v1.serializers.review import ReviewSerializer


class CarSerializer(serializers.ModelSerializer):
    raiting = RaitinSerializer(many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Car
        exclude = ['is_published']
