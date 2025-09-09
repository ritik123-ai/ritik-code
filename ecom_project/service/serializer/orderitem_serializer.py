from rest_framework  import serializers
from service.models import OrderItem
from service.serializer import ProductSerializer



class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'total_price']
