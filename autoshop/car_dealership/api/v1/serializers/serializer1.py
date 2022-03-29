from rest_framework import serializers

from core.serializers import AbstractDefaultSerializers


class CarSerializer(AbstractDefaultSerializers):
    title = serializers.CharField()
    content = serializers.CharField()
    year = serializers.IntegerField()
    price = serializers.IntegerField()
    curenncy = serializers.CharField()
    cat = serializers.CharField()
