from rest_framework import serializers

from supplier.models import *


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        exclude = ['is_published']
