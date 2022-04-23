from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil



# Create your tests here.
def index(request):
    # Products = Product.objects.all()
    
    # n = len(Products)
    # nSlides = n//4 +ceil((n/4) - (n//4))
    # allprod = [[Products,range(1,nSlides), nSlides],#len(Products)
    #            [Products,range(1,nSlides), nSlides]]

    allprod  = []
    catprod = Product.objects.values('category')
    # print(catprod)
    cats = {item['category'] for item in catprod}
    # print(cats)
    for cat in cats:
        prod = Product.objects.filter(category = cat)
        n = len(prod)
        nSlides = n//4 +ceil((n/4) - (n//4))
        allprod.append([prod,range(1,nSlides), nSlides])



    params = {"allprods":allprod}
    # params = {"no_of slides": nSlides,"range": range(1,nSlides),"products" : Products}
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





