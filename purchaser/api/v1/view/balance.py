from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions


from car_dealership.api.v1.view.car import APIListPagination
from core.filters.purchaser import BalanceFilters
from purchaser.api.v1.serializers.balance import BalanceSerialazer
from purchaser.models import Balance


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerialazer
    pagination_class = APIListPagination
    permission_classes = [permissions.IsAdminUser, ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BalanceFilters
    search_fields = ['value']
