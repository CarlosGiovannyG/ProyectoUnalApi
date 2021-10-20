from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin, UserManager
from simple_history.models import HistoricalRecords

class UserManage(BaseUserManager):

  def _create_user(self, username,email,last_name,password,is_staff,is_superuser,**extra_fields):
    user = self.model(
      username = username,
      email = email,
      last_name = last_name,
      is_staff = is_staff,
      is_superuser = is_superuser,
      **extra_fields
    )

    user.set_password(password)
    user.save(using=self.db)
    return user


  def create_user(self, username, email,name, last_name,password=None,**extra_fileds):

    return self._create_user(username,email,name,last_name,password=None,**extra_fileds)

  def create_superuser(self,username,email,name,last_name,password=None,**extra_fields):
    
    return self._create_user(username,email,name,last_name,password=True,**extra_fields)






class User(AbstractBaseUser,PermissionsMixin):
  username=models.CharField('Nombre de usuario',max_length=150,unique=True)
  email= models.EmailField('Correo electronico',max_length=150, unique=True)
  name = models.CharField('Nombre',max_length=150, blank=True,null=True)
  last_name = models.CharField('Apellido',max_length=150,blank=True,null=True)
  image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  historical = HistoricalRecords()
  objects  = UserManager()

  class Meta:
    verbose_name = 'Usuario'
    verbose_name_plural = 'Usuarios'

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ['email','name','last_name']

  def natural_key(self) :
      return (self.username)

  def __str__(self) :
      return 'Usuario {0}, con Nombre: {1} {2} '.format(self.username,self.name,self.last_name)