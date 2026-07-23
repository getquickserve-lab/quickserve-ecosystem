from django.contrib import admin
from .models import VendorProfile, Product, Order, OrderItem
admin.site.register([VendorProfile, Product, Order, OrderItem])
