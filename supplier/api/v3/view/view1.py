from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.view.view1 import APIListPagination
from supplier.api.v3.serializers.serializer1 import SupplierSerializer
from supplier.models import Supplier


class SupplierViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin, GenericViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name']
