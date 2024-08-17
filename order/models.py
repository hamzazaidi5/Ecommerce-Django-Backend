from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    total_items = models.IntegerField(default=0)  # Denormalized field

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['order_date']),
        ]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['order']),
            models.Index(fields=['product']),
        ]
