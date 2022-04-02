from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    year = serializers.IntegerField()
    price = serializers.IntegerField()
    currency = serializers.CharField()
    cat = serializers.CharField()
    status = serializers.CharField()