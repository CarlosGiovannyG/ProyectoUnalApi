
from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = '__all__'


  def create(self, validated_data):
     user = User(**validated_data)
     user.set_password(validated_data['password'])
     user.save()
     return user

  def update(self, instance, validated_data):
    update_user = super().update(instance, validated_data)
    update_user.set_password(validated_data['password'])
    update_user.save()
    return update_user


'''
SERIALIZER PARA LISTAR POR ID
'''

class UserListSerializers(serializers.ModelSerializer):
  class Meta:
    model = User

  '''
  LISYTAMNOS EN LA VISTA SOLO LOS CAMPOS QUE QUEREMOS
  '''
  def to_representation(self, instance):

    return{
      'id': instance['id'],
      'Nombre de usuario': instance['username'],
      'Correo': instance['email'],
      'Nombre': instance['name'],
      'Apellido':instance['last_name'],
      'Contraseña':instance['password']
    }
     


