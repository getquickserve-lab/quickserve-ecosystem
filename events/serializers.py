from rest_framework import serializers
from .models import Event, TicketType, Ticket

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ('id', 'name', 'price', 'total_quantity', 'fee_option')

class EventSerializer(serializers.ModelSerializer):
    ticket_types = TicketTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'organizer', 'title', 'description', 'venue', 'event_date', 'slug', 'ticket_types')

class TicketSerializer(serializers.ModelSerializer):
    event_title = serializers.ReadOnlyField(source='ticket_type.event.title')
    ticket_type_name = serializers.ReadOnlyField(source='ticket_type.name')

    class Meta:
        model = Ticket
        fields = ('id', 'ticket_type', 'event_title', 'ticket_type_name', 'customer', 'ticket_code', 'is_used')
        read_only_fields = ('id', 'customer', 'ticket_code', 'is_used')
