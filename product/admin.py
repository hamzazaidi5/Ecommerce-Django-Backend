from django.contrib import admin
from .models import Product, ProductRecommendation, Category

class MyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, MyModelAdmin)
admin.site.register(ProductRecommendation, MyModelAdmin)
admin.site.register(Category, MyModelAdmin)
