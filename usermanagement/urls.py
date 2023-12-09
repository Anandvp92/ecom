from django.urls import path,include
from .views import *
urlpatterns = [
    path('login/',userlogin,name="login"),
    path('register/',register,name="register"),
    path('logout/',logout,name="logout"),
    
]