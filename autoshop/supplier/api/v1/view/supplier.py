from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.view.car import APIListPagination
from core.filters.supplier import SupplierFilters
from core.permissions import IsAdminOrReadOnly
from supplier.api.v1.serializers.supplier import SupplierSerializer
from supplier.models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilters
    search_fields = ['name']
