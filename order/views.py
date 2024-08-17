from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from order.models import Order, OrderItem
from order.serializers import OrderSerializer, OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)