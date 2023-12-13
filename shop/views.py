from django.shortcuts import render,redirect
from .forms import productform
from django.http import HttpResponse
from .models import productmodel
import os

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


def listproduct(request):
    products= productmodel.objects.all()
    return render(request,"productlist.html",{"products":products})


def deleteproduct(request,pk):
    isinstances= productmodel.objects.get(pk=pk)    
    if isinstances.IMAGE:
        os.remove(isinstances.IMAGE.path)   
    isinstances.delete() 
    return redirect("index")


def editproduct(request,pk):
    obj = productmodel.objects.get(id=pk)
    if request.POST:
        insc= productform(data=request.POST,files=request.FILES,instance=obj)
        if insc.is_valid:
            insc.save()
            return redirect('shop')
    else:
        insc=productform(instance=obj)
    return render(request,"edit.html",{"form":insc})
