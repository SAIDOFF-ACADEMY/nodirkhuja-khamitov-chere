from common import serializers
from common.model import setting, page, gallery
import time

from rest_framework.response import Response
from rest_framework import generics, permissions

from django.utils.translation import gettext_lazy as _


class SettingsView(generics.GenericAPIView):
    queryset = setting.Setting.objects.all()
    serializer_class = serializers.SettingSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data)
    
    def put(self, request):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PageListView(generics.ListAPIView):
    queryset = page.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [permissions.IsAdminUser]


class AddPageView(generics.CreateAPIView):
    queryset = page.Page.objects.all()
    serializer_class = serializers.PageSerializer
    permission_classes = [permissions.IsAdminUser]


class RetrievePageView(generics.RetrieveAPIView):
    queryset = page.Page.objects.all()
    serializer_class = serializers.PageSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]


class EditPageView(generics.UpdateAPIView):
    queryset = page.Page.objects.all()
    serializer_class = serializers.PageSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]


class DeletePageView(generics.DestroyAPIView):
    queryset = page.Page.objects.all()
    serializer_class = serializers.PageSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAdminUser]

class ListGalleryView(generics.ListAPIView):
    queryset = gallery.GalleryPhoto.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [permissions.IsAdminUser]


class AddGalleryView(generics.CreateAPIView):
    queryset = gallery.GalleryPhoto.objects.all()
    serializer_class = serializers.GallerySerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, reqeust, *args, **kwargs):
        t1 = time.perf_counter()
        resp = super(AddGalleryView, self).post(reqeust,*args, **kwargs)
        print(time.perf_counter()-t1)
        return Response({})

class DeleteGalleryView(generics.DestroyAPIView):
    queryset = gallery.GalleryPhoto.objects.all()
    serializer_class = serializers.GallerySerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAdminUser]


