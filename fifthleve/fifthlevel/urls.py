from django.urls import path
from fifthlevel import views

app_name= 'fifthlevel'
urlpatterns= [
    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login')
]
