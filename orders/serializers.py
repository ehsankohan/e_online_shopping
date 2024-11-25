from rest_framework import serializers
from .models import Order,OrderItem
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    
    product = ProductSerializer(serializers.ModelSerializer)
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'items']
