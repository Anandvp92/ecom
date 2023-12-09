from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as li,logout as lo
# Create your views here.

def userlogin(request):
    user=None
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)    
        print(user)
        if user:
            li(request,user)
            
            return redirect("index")
        if user is None:
            return render(request,"login.html",context={'error_message':"Username Or Password Is Wrong!"})                      
    return render(request,"login.html")

def register(request):
    if request.POST:
        username=request.POST['username']      
        email=request.POST['email']
        password=request.POST['password']
        try:
            if username and email and password:
                User.objects.create_user(username=username,password=password,email=email)
                return redirect("index")
        except Exception as e:
            print(e)
            
    return render(request,"login.html")


def logout(request):
    lo(request)
    return redirect("login")
