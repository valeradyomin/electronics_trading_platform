from rest_framework.routers import DefaultRouter

from distributors.apps import DistributorsConfig
from distributors.views import SupplierViewSet, ProductViewSet

app_name = DistributorsConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'products', ProductViewSet, basename='products')

urlpatterns = [] + router.urls