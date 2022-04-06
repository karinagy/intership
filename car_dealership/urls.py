from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from car_dealership.api.v1.view.view1 import CarViewSet
from car_dealership.api.v1.view.view2 import CategoryViewSet
from car_dealership.api.v1.view.view3 import ReviewViewSet
from car_dealership.api.v1.view.view4 import Car_dealershipViewSet
from car_dealership.api.v1.view.view5 import RaitingViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'car_dealership', Car_dealershipViewSet)
router.register(r'raiting', RaitingViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('api/v1/', include(router.urls)),

]
