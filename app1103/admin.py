from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app1103.models import Product, ProductTag


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass


@admin.register(ProductTag)
class ProductTagAdmin(ModelAdmin):
    pass
