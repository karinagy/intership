# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from car_dealership.api.v1.serializers.car import CarSerializer
from car_dealership.models import Car
from core.filters.car_dealership import CarFilters
from core.permissions import IsAdminOrReadOnly


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = CarFilters
    ordering_fields = ['title', 'year']
    search_fields = ['name', 'status']

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()
