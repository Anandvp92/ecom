from django.shortcuts import render,redirect
from .forms import productform
from django.http import HttpResponse
from .models import productmodel

# Create your views here.

def createproduct(request):
    if request.POST:
        form = productform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("shop")
        else:
            # If the form has errors, you might want to display them
            print(form.errors) 
    return render(request,"create.html",context={"form":productform})


def editproduct(request):
    products= productmodel.objects.all()
    return render(request,"edit.html",{"products":products})


def deleteproduct(request):
    return render(request,"delete.html")