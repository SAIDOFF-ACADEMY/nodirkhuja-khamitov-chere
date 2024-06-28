from django.contrib import admin
from .models import Product
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass