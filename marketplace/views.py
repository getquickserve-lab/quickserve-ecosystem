from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import VendorProfile, Product, Order
from .serializers import VendorProfileSerializer, ProductSerializer, OrderSerializer

# --- PUBLIC / CONSUMER VIEWS ---
class VendorProfileListCreateView(generics.ListCreateAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        vendor = self.request.user.vendor_profile
        serializer.save(vendor=vendor)

class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)

class OrderCancelView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user, status='PENDING')

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        order.status = 'CANCELLED'
        order.save()
        return Response({'status': 'Order cancelled successfully'}, status=status.HTTP_200_OK)


# --- VENDOR PORTAL VIEWS ---
class VendorProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Allows vendors to update price, inventory stock, or delete their own products"""
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(vendor__user=self.request.user)

class VendorOrderListView(generics.ListAPIView):
    """Allows vendors to view all incoming orders placed at their store"""
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(vendor__user=self.request.user).order_by('-created_at')

class VendorOrderStatusUpdateView(generics.UpdateAPIView):
    """Allows vendors to update order status (e.g., PENDING -> PREPARING -> READY)"""
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(vendor__user=self.request.user)

    def update(self, request, *args, **kwargs):
        order = self.get_object()
        new_status = request.data.get('status')
        if new_status:
            order.status = new_status
            order.save()
            return Response({'status': f'Order status updated to {new_status}'}, status=status.HTTP_200_OK)
        return Response({'error': 'No status provided'}, status=status.HTTP_400_BAD_REQUEST)
