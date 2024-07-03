from rest_framework import serializers
from user.models import User
from user.models import UserContactApplication

class LogInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model=User
        fields=('email', 'password')

        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
        }


class UserContacApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserContactApplication
        fields=[
            'full_name',
            'phone_number',
            'user',
        ]