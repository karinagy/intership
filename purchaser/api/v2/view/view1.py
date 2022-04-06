from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.view.view1 import APIListPagination
from purchaser.api.v2.serializers.serializer1 import PurchaserSerialazer
from purchaser.models import Purchaser


class PurchaserViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       GenericViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerialazer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'surname']
