from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your tests here.
def index(request):
    params = {}
    Products = Product.objects.all()
    return render(request, 'shop/index.html',params)


def about(request):
    return HttpResponse("we are at about")



def contact(request):
    return HttpResponse("we are at contact")



def tracker(request):
    return HttpResponse("we are at tracker")



def search(request):
    return HttpResponse("we are at search")



def productview(request):
    return HttpResponse("we are at productview")


def checkout(request):
    return HttpResponse("we are at checkout")





