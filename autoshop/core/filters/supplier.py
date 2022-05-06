from django_filters import rest_framework as filters

from supplier.models import Supplier, Raiting, Founder


class SupplierFilters(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Supplier
        fields = ['name', 'location']


class RaitingFilters(filters.FilterSet):
    value = filters.RangeFilter()

    class Meta:
        model = Raiting
        fields = ['value']


class FounderFilters(filters.FilterSet):
    first_name = filters.CharFilter()
    second_name = filters.CharFilter()

    class Meta:
        model = Founder
        fields = ['first_name', 'second_name']
