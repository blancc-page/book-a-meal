from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField("email address", unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]
    is_customer = models.BooleanField(default=False)
    is_caterer = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Caterer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)


