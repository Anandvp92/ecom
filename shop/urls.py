from django.urls import path
from .views import *
urlpatterns = [
    path('create/',createproduct,name="create"),
    path('list/',listproduct,name="list"),
    path('delete/<pk>',deleteproduct,name="delete"),
    path('edit/<pk>',editproduct,name="edit"),
    path('test/',testfun,name="test"),
    
]