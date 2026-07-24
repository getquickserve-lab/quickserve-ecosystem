from rest_framework import serializers
from .models import VendorProfile, Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'vendor', 'name', 'description', 'price', 'stock', 'is_available')
        read_only_fields = ('id', 'vendor')

class VendorProfileSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = VendorProfile
        fields = ('id', 'user', 'business_name', 'category', 'address', 'is_verified', 'commission_rate', 'products')
        read_only_fields = ('id', 'user', 'is_verified', 'commission_rate')

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'product_name', 'quantity', 'price')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'customer', 'vendor', 'total_amount', 'status', 'created_at', 'items')
        read_only_fields = ('id', 'customer', 'status', 'created_at')
