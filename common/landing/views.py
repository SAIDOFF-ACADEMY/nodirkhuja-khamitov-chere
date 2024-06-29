from rest_framework import generics
from rest_framework.response import Response

from common.landing import serializers
from common.model import setting, page, gallery


class SettingsView(generics.GenericAPIView):
    queryset = setting.Setting.objects.all()
    serializer_class = serializers.SettingsSerializer

    def get(self, request):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)

class RetrievePageView(generics.RetrieveAPIView):
    queryset = page.Page.objects.all()
    serializer_class = serializers.LandingPageSerializer
    lookup_field = 'slug'


class ListGalleryView(generics.ListAPIView):
    queryset = gallery.GalleryPhoto.objects.order_by('?')
    serializer_class = serializers.GallerySerializer