from django.urls import path
from .views import DeliveryRequestListCreateView, DeliveryCancelView

urlpatterns = [
    path('deliveries/', DeliveryRequestListCreateView.as_view(), name='delivery_list_create'),
    path('deliveries/<int:pk>/cancel/', DeliveryCancelView.as_view(), name='delivery_cancel'),
]
