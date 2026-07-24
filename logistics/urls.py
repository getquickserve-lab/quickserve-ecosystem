from django.urls import path
from .views import (
    DeliveryRequestListCreateView, 
    DeliveryCancelView,
    AvailableDeliveriesListView,
    AcceptDeliveryView,
    RiderActiveDeliveriesView,
    UpdateDeliveryStatusView
)

urlpatterns = [
    # Consumer Routes
    path('deliveries/', DeliveryRequestListCreateView.as_view(), name='delivery_list_create'),
    path('deliveries/<int:pk>/cancel/', DeliveryCancelView.as_view(), name='delivery_cancel'),

    # Rider Routes
    path('rider/available/', AvailableDeliveriesListView.as_view(), name='rider_available_deliveries'),
    path('rider/accept/<int:pk>/', AcceptDeliveryView.as_view(), name='rider_accept_delivery'),
    path('rider/active/', RiderActiveDeliveriesView.as_view(), name='rider_active_deliveries'),
    path('rider/status/<int:pk>/', UpdateDeliveryStatusView.as_view(), name='rider_update_status'),
]
