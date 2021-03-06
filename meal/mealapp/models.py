from django.db import models
from django.contrib.auth.models import User


# Create your models here

def upload_path(instance, filename):
    return '/'.join(['menu', str(instance.name), filename])

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Caterer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Menu(models.Model):
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True )
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, default='')
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True, blank=True)

    def get_menu_count_by_menu_id(self, menu_id):
        return self.objects.filter(menu_id=menu_id).count()

    def __str__(self):
        return str(self.menu.price)
    
    

