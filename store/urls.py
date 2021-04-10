from django.urls import path, include
from . import views
from main import views as mainViews

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/<str:name>', views.product, name='product'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart/<str:name>', views.add_to_cart, name='add_to_cart')
]