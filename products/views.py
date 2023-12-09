from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def indexpage(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def shop(request):
    return render(request,"shop.html")



def blog(request):
    return render(request,"blog.html")