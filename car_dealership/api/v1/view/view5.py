from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializers.serializer5 import RaitinSerializer
from car_dealership.api.v1.view.view1 import APIListPagination
from car_dealership.models import Raiting


class RaitingViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Raiting.objects.all()
    serializer_class = RaitinSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['value']
