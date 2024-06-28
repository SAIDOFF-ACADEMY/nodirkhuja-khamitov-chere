from rest_framework import serializers
from common.model import Setting
from user.models import User_Profile

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Setting
        fields='__all__'


class LogInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model=User_Profile
        fields=('email', 'password')