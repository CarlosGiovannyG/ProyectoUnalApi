from productos.models import MeasureUnit,CategoryProduct,Indicator
from rest_framework import fields, serializers

class MeasureUnitSerializer(serializers.ModelSerializer):

  class Meta:
    model=MeasureUnit
    #fields='__all__'
    #exclude=('state',)
    exclude=('state','created_date','modified_date','deleted_date')


class CategoryProductSerializer(serializers.ModelSerializer):

  class Meta:
    model=CategoryProduct
    exclude=('state',)
    


class IndicatorSerializer(serializers.ModelSerializer):

  class Meta:
    model=Indicator
    exclude=('state',)
