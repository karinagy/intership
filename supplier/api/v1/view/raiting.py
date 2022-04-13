from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.view.car import APIListPagination
from core.filters.supplier import RaitingFilters
from supplier.api.v1.serializers.raiting import RaitingSerializer
from supplier.models import Raiting


class RaitingSupplierViewSet(viewsets.ModelViewSet):
    queryset = Raiting.objects.all()
    serializer_class = RaitingSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = RaitingFilters
    search_fields = ['value']
