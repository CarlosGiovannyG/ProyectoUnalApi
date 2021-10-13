from django.db import models

# Create your models here.

class ModeloBase(models.Model):

  id=models.AutoField(primary_key=True)
  state=models.BooleanField('Estado',default=True)
  created_date=models.DateField('Fecha creacion',auto_now=False,auto_now_add=True)
  modified_date=models.DateField('Fecha modificacion',auto_now=True,auto_now_add=False)
  deleted_date=models.DateField('Fecha eliminacion',auto_now=True,auto_now_add=False)


  class Meta:
    abstract=True
    verbose_name='Modelo Base'
    verbose_name_plural='Modelos Base'