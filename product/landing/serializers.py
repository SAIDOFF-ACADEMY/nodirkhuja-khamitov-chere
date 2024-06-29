from rest_framework import serializers
from product.models import Product

class LandingProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Product
        fields=[
            'id',
            'name_uz',
            'name_ru',
            'content_ru',
            'content_uz',
            'price',
            'order'
            ]