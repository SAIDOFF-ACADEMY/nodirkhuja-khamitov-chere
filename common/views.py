from common import serializers
from common.model import setting
from user.models import User_Profile

from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth import authenticate, login
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
    
class LogInView(generics.GenericAPIView):
    queryset = User_Profile.objects.all()
    serializer_class = serializers.LogInSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token = Token.objects.get(user=user)
            login(request, user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': _('Invalid Credentials')}, status=status.HTTP_400_BAD_REQUEST)
        