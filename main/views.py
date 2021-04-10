from django.shortcuts import render
from .models import *

# Create your views here.
def home(request): 
    return render(request, 'main/home.html', context={})

def about(request):
    return render(request, 'main/about.html', context={})

def contact(request):
    return render(request, 'main/contact.html', context={})