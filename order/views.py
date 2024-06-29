from rest_framework import generics, permissions, response

from order import serializers, models



class OrderListView(generics.ListAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrderListSerializer
    permission_classes = [permissions.IsAdminUser]


class OrderEditStatusVeiw(generics.UpdateAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrderEditStatusSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        order = self.get_object()
        serializer = self.get_serializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=user)
        return response.Response(serializer.data)

class OrderRetrieveView(generics.RetrieveAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = serializers.OrderEditStatusSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]
