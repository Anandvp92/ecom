from django.shortcuts import render,redirect

# Create your views here.

def userlogin(request):
    if request.POST:
        print(request.POST['username'])
        print(request.POST['password'])
        return redirect("index")
    return render(request,"login.html")

def register(request):
    if request.POST:
        print(request.POST['username'])        
        print(request.POST['email'])
        print(request.POST['password'])
        return redirect("index")
    return render(request,"login.html")
