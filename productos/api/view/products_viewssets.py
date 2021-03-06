from rest_framework import generics, serializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


from base.api import GeneralListApiView
from productos.api.serializers.product_serializers import ProductSerializer
from users.authentication_mixin import Authetication



'''MODO DE TRABAJO CON VIWSET ESTO HACE QUE CON UNA SOLA RUTA SE HAGA TODO EL CRUD '''
class ProductViewSet(Authetication, viewsets.ModelViewSet):
  serializer_class = ProductSerializer


  '''SE PUEDE SOBREESCRIBIR CADA METODO QUE TRAE '''

  def get_queryset(self,pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.filter(state=True)
    return self.get_serializer().Meta.model.objects.filter(id=pk,state=True).first()



  def list(self, request):
    product_serializer = self.get_serializer(self.get_queryset(),many=True)
    return Response(product_serializer.data,status=status.HTTP_200_OK)



  # AQUI NO SE LLAMA POST SINO CREATE 

  def create(self, request):
    serializer = self.serializer_class(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response({'message': 'Producto creado correctamente'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


  def delete(self,request,pk=None):
      product=self.get_queryset().filter(id=pk).first()

      if product:
        product.state=False
        product.save()
        return Response({'message':'Producto eliminado correctamente'},status=status.HTTP_200_OK)
      return Response({'error':"No existe un producto con estos datos"},status=status.HTTP_400_BAD_REQUEST)


  def update(self, request,pk=None):
      if self.get_queryset(pk):
        product_serializer=self.serializer_class(self.get_queryset(pk),data=request.data)

        if product_serializer.is_valid():
          product_serializer.save()
          return Response(product_serializer.data,status=status.HTTP_200_OK)
      return Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


