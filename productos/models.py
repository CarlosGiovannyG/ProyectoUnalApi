from django.db import models
from simple_history.models import HistoricalRecords

from base.models import ModeloBase

# MODELO QUE VA A TENER LA UNIDAD DE MEDIDA DE LOS PRODCUTOS


class MeasureUnit(ModeloBase):

  descripton=models.CharField('Descripcion', max_length=250,blank=False,null=False,unique=True)
  historical=HistoricalRecords()

  @property
  def _history_user(self):
    return self.change_by

  @_history_user.setter
  def _hisroty_user(self,value):
    self.change_by=value

  class Meta:
    verbose_name='Unidad de Medida'
    verbose_name_plural='Unidades de Medida'

  def __str__(self):
    return self.descripton



#MODELO DE CATEGORIA 

class CategoryProduct(ModeloBase):

  description=models.CharField('Descripcion',max_length=250,unique=True,null=False,blank=False)
  historical=HistoricalRecords()

  @property
  def _history_user(self):
    return self.change_by

  @_history_user.setter
  def _hisroty_user(self,value):
    self.change_by=value

  class Meta:
    verbose_name='Categoria de Producto'
    verbose_name_plural='Categorias de Productos'

  def __str__(self):
    return self.description

#INDICAR DE OFERTAS
class Indicator(ModeloBase):

  descount_value=models.PositiveSmallIntegerField(default=0)
  categoy_product=models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name='Indicador de descuento',null=True)
  historical=HistoricalRecords()

  @property
  def _history_user(self):
    return self.change_by

  @_history_user.setter
  def _hisroty_user(self,value):
    self.change_by=value

  class Meta:
    verbose_name='Indicador de oferta'
    verbose_name_plural='Indicadores de ofertas'

  def __str__(self):
    return f'Oferta de la categoria {self.categoy_product}:{self.descount_value}%'


#MODELO PRINCIPAL

class Product(ModeloBase):

  name=models.CharField('Nombre de Producto',max_length=150,unique=True,blank=False,null=False)
  description=models.TextField('Descripcion de Producto',blank=False,null=False)
  image = models.ImageField('Imagen del Producto', upload_to='products/',blank = True,null = True)
  category_product=models.ForeignKey(CategoryProduct,on_delete=models.CASCADE,verbose_name='Categoria de Prodcuto',null=True)
  meausre_unit=models.ForeignKey(MeasureUnit,on_delete=models.CASCADE,verbose_name='Unidad de Medida',null=True)
  historical=HistoricalRecords()

  @property
  def _history_user(self):
    return self.change_by

  @_history_user.setter
  def _hisroty_user(self,value):
    self.change_by=value

  class Meta:
    verbose_name='Producto'
    verbose_name_plural='Productos'

  def __str__(self):
    return self.name
