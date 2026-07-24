from rest_framework import serializers
from .models import RiderProfile, DeliveryRequest

class DeliveryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRequest
        fields = ('id', 'sender', 'rider', 'pickup_address', 'dropoff_address', 'recipient_name', 'recipient_phone', 'delivery_fee', 'status')
        read_only_fields = ('id', 'sender', 'rider', 'status')
