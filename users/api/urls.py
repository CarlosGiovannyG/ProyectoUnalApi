from django.urls import path
from users.api.api import user_api_view,user_detail_api_view

urlpatterns = [
  path('',user_api_view,name='usuarios_api'),
  path('<int:pk>',user_detail_api_view,name='user_detail_api')  
  ]