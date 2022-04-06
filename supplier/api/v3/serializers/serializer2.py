from rest_framework import serializers

from supplier.models import *


class RaitingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raiting
        fields = ['supplier', 'value', 'time_create']
