


from rest_framework.routers import DefaultRouter
from productos.api.view.general_view import *
from productos.api.view.products_viewssets import ProductViewSet

router = DefaultRouter()

router.register(r'',ProductViewSet,basename='products')
router.register(r'meazure-unit',MeasureUnitViewSet,basename='meazure-unit')
router.register(r'indicator',IndicatorViewSet,basename='indicator')
router.register(r'category',CategoryProductViewSet,basename='category')

urlpatterns=router.urls

