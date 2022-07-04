from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'password', 'first_name', 'last_name', 'is_customer', 'is_caterer']

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']    

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Customer)
admin.site.register(Caterer)
admin.site.register(Menu)
admin.site.register(Order)