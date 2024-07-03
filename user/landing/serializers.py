from rest_framework import serializers
from user.models import UserContactApplication


class UserContacApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserContactApplication
        fields=[
            'full_name',
            'phone_number',
            'user',
        ]