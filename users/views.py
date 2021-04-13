from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import registerForm, loginForm

# Create your views here.
def signout(request):
    logout(request)
    messages.info = 'You have been signed out.'
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success = 'Welcome ' + username
            print(messages.success)
            return redirect('home')
    else:
        form = registerForm()
    return render(request, 'users/register.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success = 'Welcome ' + username
            print(messages.success)
            return redirect('home')
    else:
        form = loginForm()
    return render(request, 'users/login.html', {'form': form})