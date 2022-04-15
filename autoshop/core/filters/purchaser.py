from django_filters import rest_framework as filters

from purchaser.models import Purchaser, Balance


class PurchaserFilters(filters.FilterSet):
    first_name = filters.CharFilter()
    second_name = filters.CharFilter()

    class Meta:
        model = Purchaser
        fields = ['first_name', 'second_name']


class BalanceFilters(filters.FilterSet):
    value = filters.RangeFilter()

    class Meta:
        model = Balance
        fields = ['value']
