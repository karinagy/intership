from django.urls import path, include
from rest_framework.routers import DefaultRouter

from supplier.api.v3.view.view1 import SupplierViewSet
from supplier.api.v3.view.view2 import RaitingSupplierViewSet
from supplier.api.v3.view.view3 import FounderViewSet

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'raitingsuppliers', RaitingSupplierViewSet)
router.register(r'founders', FounderViewSet)

urlpatterns = router.urls
urlpatterns = [
    path('api/v3/', include(router.urls)),

]
