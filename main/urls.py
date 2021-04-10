from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('store/', include('store.urls'), name='catalog'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
