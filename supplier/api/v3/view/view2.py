from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.view.view1 import APIListPagination
from supplier.api.v3.serializers.serializer2 import RaitingSerializer
from supplier.models import Raiting


class RaitingSupplierViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             mixins.DestroyModelMixin,
                             GenericViewSet):
    queryset = Raiting.objects.all()
    serializer_class = RaitingSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['value']
