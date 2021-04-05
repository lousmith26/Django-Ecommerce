from django.shortcuts import render
from .models import *
from cart.cart import Cart

# Create your views here.
def cart_add(request, id):
    cart  = Cart(request)
    product = request.path()
    print(product + ' Added to cart!')

def home(request): 
    return render(request, 'main/home.html', context={})

def store(request):
    context = {
        'shirts': Shirt.objects.all(),
        'shoes': Shoe.objects.all(),
        'pants': Pant.objects.all()
    }
    return render(request, 'main/store.html', context=context)

def about(request):
    return render(request, 'main/about.html', context={})

def contact(request):
    return render(request, 'main/contact.html', context={})