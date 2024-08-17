from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import (
    ProductViewSet,
    ProductRecommendationViewSet,
    CategoryViewSet
)

router = DefaultRouter()


router.register("product", ProductViewSet)
router.register("recommendation", ProductRecommendationViewSet)
router.register("category", CategoryViewSet)
app_name = "product"

urlpatterns = [
    path("", include(router.urls)),
]
