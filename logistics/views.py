from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import DeliveryRequest
from .serializers import DeliveryRequestSerializer

# --- CONSUMER VIEWS ---
class DeliveryRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeliveryRequest.objects.filter(sender=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class DeliveryCancelView(generics.UpdateAPIView):
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeliveryRequest.objects.filter(sender=self.request.user, status='PENDING')

    def update(self, request, *args, **kwargs):
        delivery = self.get_object()
        delivery.status = 'CANCELLED'
        delivery.save()
        return Response({'status': 'Delivery request cancelled successfully'}, status=status.HTTP_200_OK)


# --- RIDER PORTAL VIEWS ---
class AvailableDeliveriesListView(generics.ListAPIView):
    """Lists all pending delivery jobs available for riders to accept"""
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeliveryRequest.objects.filter(status='PENDING').order_by('-id')

class AcceptDeliveryView(generics.UpdateAPIView):
    """Allows an authenticated rider to accept an open delivery job"""
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeliveryRequest.objects.filter(status='PENDING')

    def update(self, request, *args, **kwargs):
        delivery = self.get_object()
        delivery.rider = request.user
        delivery.status = 'ACCEPTED'
        delivery.save()
        return Response({'status': 'Delivery job accepted successfully'}, status=status.HTTP_200_OK)

class RiderActiveDeliveriesView(generics.ListAPIView):
    """Lists all active or historical deliveries claimed by the authenticated rider"""
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeliveryRequest.objects.filter(rider=self.request.user).order_by('-id')

class UpdateDeliveryStatusView(generics.UpdateAPIView):
    """Allows riders to update active job statuses (e.g. IN_TRANSIT, DELIVERED)"""
    serializer_class = DeliveryRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DeliveryRequest.objects.filter(rider=self.request.user)

    def update(self, request, *args, **kwargs):
        delivery = self.get_object()
        new_status = request.data.get('status')
        if new_status:
            delivery.status = new_status
            delivery.save()
            return Response({'status': f'Delivery status updated to {new_status}'}, status=status.HTTP_200_OK)
        return Response({'error': 'No status provided'}, status=status.HTTP_400_BAD_REQUEST)
