
from base.api import GeneralListApiView
from productos.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer,CategoryProductSerializer



class MeasureUnitListAPIView(GeneralListApiView):
  serializer_class=MeasureUnitSerializer  


class IndicatorListAPIView(GeneralListApiView):
  serializer_class=IndicatorSerializer


class CategoryProductListAPIView(GeneralListApiView):
  serializer_class=CategoryProductSerializer  


  