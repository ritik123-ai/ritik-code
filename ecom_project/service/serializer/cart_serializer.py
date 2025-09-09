
from rest_framework import serializers
from service.models import Cart
from service.serializer.cartitem_serializer import CartItemSerializer



class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'created_at']