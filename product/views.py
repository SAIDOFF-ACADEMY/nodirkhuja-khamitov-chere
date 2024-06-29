from product import serializers
from product import models

from rest_framework.response import Response
from rest_framework import generics, permissions

from django.utils.translation import gettext_lazy as _

class ListProductsView(generics.ListAPIView):
    queryset = models.Product.objects.filter(is_active=True)
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAdminUser]


class AddProductView(generics.CreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class UpdateProductView(generics.UpdateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]


class RetriveProductView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]


class DeleteProductView(generics.DestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]


class FreeProductListView(generics.ListAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductSerializer
    permission_classes = [permissions.IsAdminUser]


class FreeProductAdd(generics.CreateAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductSerializer
    permission_classes = [permissions.IsAdminUser]


class FreeProductRetriveView(generics.RetrieveAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]


class FreeProductEdit(generics.UpdateAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]


class FreeProductDelete(generics.DestroyAPIView):
    queryset = models.FreeProduct.objects.all()
    serializer_class = serializers.FreeProductSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAdminUser]