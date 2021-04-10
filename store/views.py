from django.shortcuts import render, redirect
from django.contrib import messages
from store.models import *

# Create your views here.
def catalog(request):
    context = {
        'shirts': Product.objects.filter(category='1'),
        'pants': Product.objects.filter(category='2'),
        'shoes': Product.objects.filter(category='3'),
        'messages': messages
    }
    return render(request, 'main/store.html', context=context)

def product(request, name):
    product = Product.objects.filter(name=name)
    product = product[0]
    print(product.category)
    context = {
        'product': product
    }
    return render(request, 'main/product.html', context=context)

def add_to_cart(request, name):
    if 'cart' not in request.session:
        print('The cart is not init. Init now.')
        request.session['cart'] = []
    request.session['cart'].append(name)
    messages.success = name + ' was added to your cart.'
    print(request.session['cart'])
    context = {
        'shirts': Product.objects.filter(category='1'),
        'pants': Product.objects.filter(category='2'),
        'shoes': Product.objects.filter(category='3'),
    }
    return redirect('catalog')