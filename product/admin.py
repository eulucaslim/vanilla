from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ('name_product', 'description', 'price', 'quant')