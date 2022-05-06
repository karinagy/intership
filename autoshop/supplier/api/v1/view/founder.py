from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from car_dealership.api.v1.view.car import APIListPagination
from core.filters.supplier import FounderFilters
from core.permissions import IsAdminOrReadOnly
from supplier.api.v1.serializers.founder import FounderSerializer
from supplier.models import Founder


class FounderViewSet(viewsets.ModelViewSet):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = FounderFilters
    search_fields = ['first_name', 'second_name']
