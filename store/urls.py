from django.urls import path, include
from . import views
from main import views as mainViews

urlpatterns = [
    path('', views.catalog),
    path('product/<str:name>', views.product, name='product'),
    path('add_to_cart/<str:name>', mainViews.cart_add, name='cart_add'),
]