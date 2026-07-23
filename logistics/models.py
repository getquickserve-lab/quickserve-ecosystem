from django.db import models
from django.conf import settings
class RiderProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rider_profile')
    vehicle_type = models.CharField(max_length=50)
    license_plate = models.CharField(max_length=20)
    is_available = models.BooleanField(default=False)
class DeliveryRequest(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_deliveries')
    rider = models.ForeignKey(RiderProfile, on_delete=models.SET_NULL, null=True, blank=True)
    pickup_address = models.TextField()
    dropoff_address = models.TextField()
    recipient_name = models.CharField(max_length=100)
    recipient_phone = models.CharField(max_length=15)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='SEARCHING')
