from django.urls import path
from productos.api.view.general_view import IndicatorListAPIView, MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView


urlpatterns=[  
  path('unidad_medida/',MeasureUnitListAPIView.as_view(),name='unidad_medida_view'),
  path('ofertas/',IndicatorListAPIView.as_view(),name='ofertas_view'),
  path('categoria/',CategoryProductListAPIView.as_view(),name='categoria_view'),
]

