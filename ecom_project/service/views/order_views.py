from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from service.models import Order
from service.serializer.order_serializer import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = []

    @action(detail=True, methods=['get'])
    def track(self, request, pk=None):
        order = self.get_object()
        return Response({'status': order.status, 'total_price': order.total_price})

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        if order.status in ['Pending', 'Processing']:
            order.status = 'Cancelled'
            order.save()
            return Response({'message': 'Order cancelled successfully'})
        return Response({'error': 'Cannot cancel completed or cancelled orders'}, status=status.HTTP_400_BAD_REQUEST)
