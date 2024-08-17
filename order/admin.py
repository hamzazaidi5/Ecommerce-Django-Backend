from django.contrib import admin
from .models import Order, OrderItem

class MyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Order, MyModelAdmin)
admin.site.register(OrderItem, MyModelAdmin)
