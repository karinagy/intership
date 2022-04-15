from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.serializers.car_dealership import Car_dealershipSerializer
from car_dealership.api.v1.view.car import APIListPagination
from car_dealership.models import Car_dealership
from core.filters.car_dealership import Car_dealershipFilters
from core.permissions import IsOwnerOrReadOnly


class Car_dealershipViewSet(viewsets.ModelViewSet):
    queryset = Car_dealership.objects.all()
    serializer_class = Car_dealershipSerializer
    pagination_class = APIListPagination
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = Car_dealershipFilters
    search_fields = ['name', 'characteristic']
