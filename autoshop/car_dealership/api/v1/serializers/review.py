from rest_framework import serializers


from car_dealership.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['name', 'text', 'car', 'time_create']
