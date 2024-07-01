from rest_framework import serializers
from user import models

class UserContacApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.User_Profile
        fields=[
            'full_name',
            'email',
            'telegram_id',
            'language'
        ]