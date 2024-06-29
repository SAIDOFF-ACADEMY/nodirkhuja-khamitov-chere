from rest_framework import serializers
from common.model import Setting, Page, GalleryPhoto


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Setting
        fields='__all__'


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Page
        fields='__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=GalleryPhoto
        fields=['photo']