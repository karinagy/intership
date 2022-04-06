from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from car_dealership.api.v1.serializers.serializer3 import RewiewSerializer
from car_dealership.api.v1.view.view1 import APIListPagination
from car_dealership.models import Rewiew


# можно добавить, удалить отзыв(только для авторизованных пользователей)
class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Rewiew.objects.all()
    serializer_class = RewiewSerializer
    pagination_class = APIListPagination
    filter_backends = [DjangoFilterBackend]
    search_fields = ['car']
    # permissions = для авторизованных пользователей
