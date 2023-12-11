from django.urls import path
from .views import *
urlpatterns = [
    path('create/',createproduct,name="create"),
    path('update/',editproduct,name="edit"),
    path('delete/',deleteproduct,name="delete"),
]