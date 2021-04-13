from django.db import models
from users.models import Profile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product.name

class Cart(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(CartItem)