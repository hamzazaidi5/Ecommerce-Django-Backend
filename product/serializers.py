from rest_framework import serializers
from product.models import Product, Category, ProductRecommendation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock_quantity', 'categories']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']

class ProductRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRecommendation
        fields = ['id', 'product', 'recommended_product']