from django.db import models
from django.utils.text import slugify

# Create your models here.
class Shirt(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    sizes = [
        ('SMALL', 'S'),
        ('MEDIUM', 'M'),
        ('LARGE', 'L'),
        ('X-LARGE', 'XL')
    ]
    size = models.CharField(choices=sizes, max_length=7, blank=True)
    type = 1

    def __str__(self):
        return self.name

class Pant(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    sizes = [
        ('SMALL', 'S'),
        ('MEDIUM', 'M'),
        ('LARGE', 'L'),
        ('X-LARGE', 'XL')
    ]
    size = models.CharField(choices=sizes, max_length=7, blank=True)
    type = 2

    def __str__(self):
        return self.name
 
class Shoe(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    sizes = [
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12')
    ]
    size = models.CharField(choices=sizes, max_length=7, blank=True)
    type = 3

    def __str__(self):
        return self.name

class Customer(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.lastName
