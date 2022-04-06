from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializers.serializer2 import CategorySerializer
from car_dealership.api.v1.view.view1 import APIListPagination
from car_dealership.models import Category


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']
