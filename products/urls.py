from django.urls import path
from .views import *
urlpatterns = [
    path('',indexpage,name="index"),
    path('about/',about,name="about"),
    path('products/',shop,name="shop"),
    path('blog/',blog,name="blog"),
    path('login/',about,name="login"),
    path('register/',about,name="register"),
    path('cart/',cart,name="cart"),

]