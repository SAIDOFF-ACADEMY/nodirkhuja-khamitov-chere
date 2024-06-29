from rest_framework import serializers
from product import models

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Product
        fields=[
            'id',
            'name_uz',
            'name_ru',
            'content_ru',
            'content_uz',
            'price',
            'order'
            ]
        
        extra_kwargs = {
            'name_ru': {'required': True},
            'name_uz': {'required': True},
            'content_ru': {'required': True},
            'content_uz': {'required': True}
        }

class FreeProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.FreeProduct
        fields=[
            'id',
            'product',
            'count',
            'free_count'
            ]
        
        extra_kwargs = {
            'product': {'required': True},
            'count': {'required': True},
            'free_count': {'required': True},
        }