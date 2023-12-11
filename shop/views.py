from django.shortcuts import render
from .forms import productform
# Create your views here.

def createproduct(request):
    return render(request,"create.html",context={"form":productform})


def editproduct(request):
    return render(request,"edit.html")


def deleteproduct(request):
    return render(request,"delete.html")