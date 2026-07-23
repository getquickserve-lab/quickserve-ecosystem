from django.db import models
from django.conf import settings
import uuid
class Event(models.Model):
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    venue = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    slug = models.SlugField(unique=True)
class TicketType(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ticket_types')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_quantity = models.PositiveIntegerField()
    fee_option = models.CharField(max_length=10, default='PASS')
class Ticket(models.Model):
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_tickets')
    ticket_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_used = models.BooleanField(default=False)
class EventAgent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    agent_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    assigned_gate = models.CharField(max_length=50)
    auth_code = models.CharField(max_length=100, unique=True)
