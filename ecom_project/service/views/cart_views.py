from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from service.models import Cart, CartItem, Product, Order, OrderItem
from service.serializer.cart_serializer import CartSerializer

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = []

    def get_queryset(self):
        return Cart.objects.all()

    @action(detail=False, methods=['post'])
    def add_to_cart(self, request):
        username = request.data.get('username')
        user = User.objects.get(username=username)
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        product = Product.objects.get(id=product_id)
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()
        return Response({'message': 'Added to cart successfully.'})

    @action(detail=False, methods=['post'])
    def checkout(self, request):
        username = request.data.get('username')
        user = User.objects.get(username=username)
        cart = Cart.objects.get(user=user)
        if not cart.items.exists():
            return Response({'error': 'Cart is empty'}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=user)
        for item in cart.items.all():
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        cart.items.all().delete()
        return Response({'message': 'Order placed successfully', 'order_id': order.id})
