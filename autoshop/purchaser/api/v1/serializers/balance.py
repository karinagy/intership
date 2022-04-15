from purchaser.models import Balance
from rest_framework import serializers


class BalanceSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'

