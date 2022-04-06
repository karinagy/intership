from django.urls import path, include
from rest_framework.routers import DefaultRouter

from purchaser.api.v2.view.view1 import PurchaserViewSet

router = DefaultRouter()
router.register(r'purchasers', PurchaserViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('api/v2/', include(router.urls)),

]
