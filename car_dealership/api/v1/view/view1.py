# Create your views here.

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializers.serializer1 import CarSerializer
from car_dealership.models import Car


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
