from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from car_dealership.api.v1.serializers.review import ReviewSerializer
from car_dealership.api.v1.view.car import APIListPagination
from car_dealership.models import Review


# можно добавить, удалить отзыв(только для авторизованных пользователей)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    search_fields = ['car']
    # permissions = для авторизованных пользователей
