from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField('Category', related_name='products')

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['parent']),
        ]

class ProductRecommendation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recommendations')
    recommended_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='recommended_for')

    class Meta:
        indexes = [
            models.Index(fields=['product']),
            models.Index(fields=['recommended_product']),
        ]