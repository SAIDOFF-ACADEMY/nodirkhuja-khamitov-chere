from rest_framework import generics
from rest_framework.response import Response

from common.landing import serializers
from common.model import setting


class SettingsView(generics.GenericAPIView):
    queryset = setting.Setting.objects.all()
    serializer_class = serializers.SettingsSerializer

    def get(self, request):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)