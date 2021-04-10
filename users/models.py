from django.db import models
from django.contrib.auth.models import User
#from store.models import Cart

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

