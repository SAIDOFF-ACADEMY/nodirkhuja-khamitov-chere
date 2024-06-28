from rest_framework import serializers
from common.model import Setting
from user.models import User_Profile
from product.models import Product

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Setting
        fields='__all__'


class LogInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model=User_Profile
        fields=('email', 'password')


class ProductSerializer(serializers.ModelSerializer):
    
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
        
        extra_kwargs = {
            'name_ru': {'required': True},
            'name_uz': {'required': True},
            'content_ru': {'required': True},
            'content_uz': {'required': True}
        }