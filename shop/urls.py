from django.urls import path
from .views import *
urlpatterns = [
    path('create/',createproduct,name="create"),
    path('list/',listproduct,name="list"),
    path('delete/',deleteproduct,name="delete"),
    path('edit/',editproduct,name="edit"),
]