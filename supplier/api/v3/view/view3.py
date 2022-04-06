from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.view.view1 import APIListPagination
from supplier.api.v3.serializers.serializer3 import FounderSerializer

from supplier.models import Founder


class FounderViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name', 'surname']
