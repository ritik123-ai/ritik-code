from rest_framework import serializers
from service.models import Order 
from service.serializer import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'items', 'total_price', 'created_at']

        