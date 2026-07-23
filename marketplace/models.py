from django.db import models
from django.conf import settings
class VendorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vendor_profile')
    business_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    address = models.TextField()
    is_verified = models.BooleanField(default=False)
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
class Product(models.Model):
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='marketplace_orders')
    vendor = models.ForeignKey(VendorProfile, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)
