from rest_framework import generics, permissions
from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer

class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
