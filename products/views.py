from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import productmodel


# Create your views here.

def indexpage(request):
    product=productmodel.objects.all()[:4]
    return render(request,"index.html" ,context={"user":request.user,"products":product})


def about(request):
    return render(request,"about.html")

@login_required(login_url="login")
def shop(request):
    product=productmodel.objects.all()
    return render(request,"shop.html",context={"products":product})



def blog(request):
    return render(request,"blog.html")




def cart(request):
    return render(request,"cart.html")