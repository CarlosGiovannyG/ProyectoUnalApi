

from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter

from productos.api.view.products_viewssets import ProductViewSet

router = DefaultRouter()

router.register(r'',ProductViewSet,basename='products')

urlpatterns=router.urls

