from django.shortcuts import render
from .models import *

# Create your views here.
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

def product(request, name):
    try:
        product = Shirt.objects.get(name=name)
    except:
        try:
            product = Pant.objects.get(name=name)
        except:
            try: 
                product = Shoe.objects.get(name=name)
            except:
                product = None
    context = {
        'product': product
    }
    return render(request, 'main/product.html', context=context)