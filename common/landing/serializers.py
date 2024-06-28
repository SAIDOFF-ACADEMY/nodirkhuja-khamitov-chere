from common.model.setting import Setting
from rest_framework import serializers

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Setting
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
