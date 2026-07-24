from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import DeliveryRequest
from .serializers import DeliveryRequestSerializer

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
