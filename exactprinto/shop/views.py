from django.shortcuts import render

from .models import Product, Contact, Order, OrderUpdate
from math import ceil

from django.http import HttpResponse
def index(request):
    allprod = []
    catprod = Product.objects.values('category')
    cats = {item['category'] for item in catprod}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allprod.append([prod, range(1, nSlides), nSlides])
    params = {"allprods": allprod}
    return render(request, 'shop/index.html', params)


def about(request):
        return render(request, 'shop/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        desc = request.POST.get('desc', "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def tracker(request):
     return render(request, 'shop/tracker.html')


def search(request):
    return render(request, 'shop/search.html')


def products(request, p_id):
    # fetch product using id
    product = Product.objects.filter(product_id=p_id)
    params = {'product': product[0]}
    return render(request, 'shop/products.html', params)


def checkout(request):
    if request.method == 'POST':
        items_json = request.POST.get('itemsJson',"")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address1', "") + " " + request.POST.get('address2', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zip_code = request.POST.get('zip_code', "")
        phone = request.POST.get('phone', "")
        order = Order(name=name, email=email, address=address,
        city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        id = order.Order_id
        update = OrderUpdate(order_id = id, update_dec = "The order has been placed")
        update.save()
        
        thank = True
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')




