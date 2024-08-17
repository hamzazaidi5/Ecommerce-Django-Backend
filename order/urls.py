from django.urls import path, include
from rest_framework.routers import DefaultRouter
from order.views import (
    OrderViewSet, OrderItemViewSet, OrderHistoryViewSet
)

router = DefaultRouter()


router.register("order", OrderViewSet)
router.register("item", OrderItemViewSet)
router.register('order-history', OrderHistoryViewSet, basename='order-history')
app_name = "order"

urlpatterns = [
    path("", include(router.urls)),
]
