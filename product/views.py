from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from product.filter import ProductFilter
from product.models import Product, Category, ProductRecommendation
from product.serializers import ProductSerializer, CategorySerializer, ProductRecommendationSerializer
from django.core.cache import cache

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def list(self, request, *args, **kwargs):
        cache_key = 'products_list'

        filter_params = request.query_params.dict()
        if filter_params:
            cache_key += '_' + '_'.join([f"{key}={value}" for key, value in filter_params.items()])

        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        # 15 minutes
        cache.set(cache_key, response.data, timeout=60 * 15)
        return response
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductRecommendationViewSet(viewsets.ModelViewSet):
    queryset = ProductRecommendation.objects.all()
    serializer_class = ProductRecommendationSerializer