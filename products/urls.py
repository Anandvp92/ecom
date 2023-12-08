from django.urls import path,include
from .views import *
urlpatterns = [
    path('',indexpage,name="index"),
    path('about/',about,name="about"),
    path('shop/',shop,name="shop"),
    path('blog/',blog,name="blog"),
    path('login/',about,name="login"),
    path('register/',about,name="register"),
    

]