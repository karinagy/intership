from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializers.serializer4 import Car_dealershipSerializer
from car_dealership.api.v1.view.view1 import APIListPagination
from car_dealership.models import Car_dealership


class Car_dealershipViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            GenericViewSet):
    queryset = Car_dealership.objects.all()
    serializer_class = Car_dealershipSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'characteristic']
