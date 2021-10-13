from rest_framework import status

from rest_framework.response import Response

from rest_framework.decorators import api_view

from users.models import User
from users.api.serializers import UserSerializers, UserListSerializers


@api_view(['GET','POST'])
def user_api_view(request):

  if request.method =='GET':
    users = User.objects.all().values('id','username','email','name','last_name','password')
    user_serializer = UserListSerializers(users,many=True)
    return Response(user_serializer.data,status=status.HTTP_200_OK)

  if request.method =='POST':
    user_serializer = UserSerializers(data = request.data)
    
    if user_serializer.is_valid():
      user_serializer.save()
      return Response({'mensaje':'Usuario creado con exito'} ,status=status.HTTP_201_CREATED)
  return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  
  '''

FUNCION PARA BUSCAR POR PARAMETRO
'''
@api_view(['GET','PUT','DELETE'])
def user_detail_api_view(resquest,pk=None):
    '''
    se genera una ruta para esta funcion en especial
    porque debemos tomar el id
    '''
    user = User.objects.filter(id=pk).first()
    
    if user:
      if resquest.method=='GET':
        user_serializer = UserSerializers(user)
        return Response(user_serializer.data,status=status.HTTP_200_OK)

      elif resquest.method=='PUT':
        user_serializer = UserSerializers(user,data=resquest.data)

        if user_serializer.is_valid():
          user_serializer.save()

          return Response(user_serializer.data,status=status.HTTP_200_OK)

        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

      elif resquest.method=='DELETE':

          user.delete()

          return Response({'mrensaje':"Usuario eliminado"},status=status.HTTP_200_OK)

    return Response({'mensaje':'No se ha encontrado un usuario con estos datos'},status=status.HTTP_400_BAD_REQUEST)