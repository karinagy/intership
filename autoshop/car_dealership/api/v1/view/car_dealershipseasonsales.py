from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.serializers.car_dealershipseasonsales import Car_dealershipSeasonsalesSerializer
from car_dealership.api.v1.view.car import APIListPagination
from car_dealership.models import Car_dealershipSeasonsales
from core.permissions import IsAdminOrReadOnly


class Car_dealershipSeasonsalesViewSet(viewsets.ModelViewSet):
    queryset = Car_dealershipSeasonsales.objects.all()
    serializer_class = Car_dealershipSeasonsalesSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
