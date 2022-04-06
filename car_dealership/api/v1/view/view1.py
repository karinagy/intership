# Create your views here.

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializers.serializer1 import CarSerializer
from car_dealership.models import Car


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 2


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 mixins.DestroyModelMixin,
                 GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = (IsAdminOrReadOnly,)
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    ordering_fields = ['title', 'year']
    search_fields = ['name', 'status']
