from django.contrib import admin
from .models import custom_User, Products
# Register your models here.

admin.site.register(custom_User)
admin.site.register(Products)
# admin.site.register(Orders)
