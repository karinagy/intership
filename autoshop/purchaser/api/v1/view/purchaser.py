from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.view.car import APIListPagination
from core.filters.purchaser import PurchaserFilters
from purchaser.api.v1.serializers.purchaser import PurchaserSerialazer
from purchaser.models import Purchaser


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerialazer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaserFilters
    search_fields = ['name', 'surname']
