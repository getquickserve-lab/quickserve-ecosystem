from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    ROLE_CHOICES = (('CUSTOMER', 'Customer'), ('VENDOR', 'Vendor'), ('RIDER', 'Rider'), ('ORGANIZER', 'Event Organizer'), ('AGENT', 'Event Agent'), ('KITCHEN', 'Kitchen Manager'), ('ADMIN', 'Administrator'))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CUSTOMER')
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
