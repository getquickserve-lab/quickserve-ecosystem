from django.urls import path
from .views import EventListView, TicketListCreateView

urlpatterns = [
    path('list/', EventListView.as_view(), name='event_list'),
    path('tickets/', TicketListCreateView.as_view(), name='ticket_list_create'),
]
