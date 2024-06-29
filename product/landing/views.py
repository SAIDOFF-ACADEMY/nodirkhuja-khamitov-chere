from product import models
from product.landing import serializers
from rest_framework import generics

class ProductListView(generics.ListAPIView):
    queryset = models.Product.objects.filter(is_active=True)
    serializer_class = serializers.LandingProductSerializer
