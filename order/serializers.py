from rest_framework import serializers

from order import models
class OrderEditStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Orders
        fields=['status']

class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Orders
        fields=[
            'owner',
            'count',
            'free_count',
            'product',
            'latitude',
            'longtitude',
            'phone_number',
            'quantity',
            'product_price',
            'status_changed_at',
            'status',
            'admin'
        ]