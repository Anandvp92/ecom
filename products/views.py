from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

def indexpage(request):
    return render(request,"index.html" ,context={"user":request.user})


def about(request):
    return render(request,"about.html")

@login_required(login_url="login")
def shop(request):
    return render(request,"shop.html")



def blog(request):
    return render(request,"blog.html")




def cart(request):
    return render(request,"cart.html")