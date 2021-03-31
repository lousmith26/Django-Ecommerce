from django.contrib import admin
from django.urls import path, re_path
from . import views
from main import models

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moms/', views.index)
]
