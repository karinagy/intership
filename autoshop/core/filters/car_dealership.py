from django_filters import rest_framework as filters

from car_dealership.models import Car, Car_dealership, Raiting
from core.enums.car_dealership_enums import Currency


class CarFilters(filters.FilterSet):
    price = filters.RangeFilter()
    currency = filters.ChoiceFilter(
        choices=Currency.choices,
    )
    year = filters.RangeFilter()

    class Meta:
        model = Car
        fields = ['price', 'currency', 'year']


class Car_dealershipFilters(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Car_dealership
        fields = ['name', 'location']


class RaitingFilters(filters.FilterSet):
    value = filters.RangeFilter()

    class Meta:
        model = Raiting
        fields = ['value']
