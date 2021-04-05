from django.shortcuts import render
from main.models import *

# Create your views here.
def catalog(request):
    context = {
        'shirts': Shirt.objects.all(),
        'shoes': Shoe.objects.all(),
        'pants': Pant.objects.all()
    }
    return render(request, 'main/store.html', context=context)

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