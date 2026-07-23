from django.contrib import admin
from .models import Event, TicketType, Ticket, EventAgent
admin.site.register([Event, TicketType, Ticket, EventAgent])
