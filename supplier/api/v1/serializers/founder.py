from rest_framework import serializers

from supplier.models import Founder


class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        exclude = ['time_update', 'is_published']
