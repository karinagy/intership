from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from car_dealership.api.v1.serializers.raiting import RaitinSerializer
from car_dealership.api.v1.view.car import APIListPagination
from car_dealership.models import Raiting
from core.filters.car_dealership import RaitingFilters


class RaitingViewSet(viewsets.ModelViewSet):
    queryset = Raiting.objects.all()
    serializer_class = RaitinSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = RaitingFilters
    search_fields = ['value']
