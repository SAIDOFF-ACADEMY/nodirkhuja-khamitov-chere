from rest_framework import generics

from user import models
from user.landing import serializers

class UserContactApplicationCreateView(generics.CreateAPIView):

    queryset = models.User_Profile.objects.all()
    serializer_class = serializers.UserContacApplicationSerializer
