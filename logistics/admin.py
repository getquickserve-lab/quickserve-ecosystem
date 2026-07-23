from django.contrib import admin
from .models import RiderProfile, DeliveryRequest
admin.site.register([RiderProfile, DeliveryRequest])
