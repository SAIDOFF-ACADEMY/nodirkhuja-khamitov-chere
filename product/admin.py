from django.contrib import admin
from .models import Product, FreeProduct
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['id', 'name_uz', 'name_ru']

@admin.register(FreeProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'count']