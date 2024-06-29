from common import model
from rest_framework import serializers


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=model.Setting
        fields = [
            'telegram', 
            'phone_number',
            'longtitude', 
            'latitude', 
            'location_text', 
            'working_hours_start', 
            'working_hours_end', 
            'telegram_bot'
            ]


class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model=model.Page
        fields=[
            'slug',
            'title',
            'content'
        ]

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=model.GalleryPhoto
        fields=['photo']