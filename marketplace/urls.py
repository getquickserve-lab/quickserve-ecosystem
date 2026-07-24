from django.urls import path
from .views import (
    VendorProfileListCreateView, 
    ProductListCreateView, 
    OrderListCreateView, 
    OrderDetailView, 
    OrderCancelView
)

urlpatterns = [
    path('vendors/', VendorProfileListCreateView.as_view(), name='vendor_list_create'),
    path('products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('orders/', OrderListCreateView.as_view(), name='order_list_create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/cancel/', OrderCancelView.as_view(), name='order_cancel'),
]
