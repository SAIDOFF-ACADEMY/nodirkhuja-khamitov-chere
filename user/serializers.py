from rest_framework import serializers
from user.models import User_Profile

class LogInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model=User_Profile
        fields=('email', 'password')

        extra_kwargs = {
            'email': {'required': True},
            'password': {'required': True},
        }