from rest_framework.routers import DefaultRouter

from car_dealership.api.v1.view.car import CarViewSet
from car_dealership.api.v1.view.car_dealership import Car_dealershipViewSet
from car_dealership.api.v1.view.car_dealershipseasonsales import Car_dealershipSeasonsalesViewSet
from car_dealership.api.v1.view.car_dealershipselling import Car_dealershipSellingViewSet
from car_dealership.api.v1.view.catrgory import CategoryViewSet
from car_dealership.api.v1.view.raiting import RaitingViewSet
from car_dealership.api.v1.view.review import ReviewViewSet
from purchaser.api.v1.view.balance import BalanceViewSet
from purchaser.api.v1.view.purchaser import PurchaserViewSet
from supplier.api.v1.view.founder import FounderViewSet
from supplier.api.v1.view.raiting import RaitingSupplierViewSet
from supplier.api.v1.view.supplier import SupplierViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'review', ReviewViewSet)
router.register(r'car_dealership', Car_dealershipViewSet)
router.register(r'car_dealershipselling', Car_dealershipSellingViewSet)
router.register(r'autoshop_season_sales', Car_dealershipSeasonsalesViewSet)
router.register(r'raiting', RaitingViewSet)
router.register(r'purchasers', PurchaserViewSet)
router.register(r'balance', BalanceViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'raitingsuppliers', RaitingSupplierViewSet)
router.register(r'founders', FounderViewSet)

urlpatterns = router.urls
