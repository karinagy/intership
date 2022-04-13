from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.serializers.car_dealershipselling import Car_dealershipSellingSerializer
from car_dealership.api.v1.view.car import APIListPagination
from car_dealership.models import Car_dealershipSelling
from core.permissions import IsOwnerOrReadOnly


class Car_dealershipSellingViewSet(viewsets.ModelViewSet):
    queryset = Car_dealershipSelling.objects.all()
    serializer_class = Car_dealershipSellingSerializer
    pagination_class = APIListPagination
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
