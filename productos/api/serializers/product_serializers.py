from rest_framework import serializers

from productos.models import Product

class ProductSerializer(serializers.ModelSerializer):


  class Meta:
    model= Product
    #exclude=('state')
    exclude=('state','created_date','modified_date','deleted_date')

  def to_representation(self, instance):
      return {
        'id':instance.id,
        'descripcion': instance.description,
        'name':instance.name,
        'image': instance.image if instance.image != '' else '',
        'measure_unit': instance.meausre_unit.descripton if instance.meausre_unit is not None else '',
        'category_products': instance.category_product.description if instance.category_product is not None else '',
      }