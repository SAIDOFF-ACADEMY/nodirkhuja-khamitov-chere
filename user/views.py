from user import serializers
from user.models import User_Profile


from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _



class LogInView(generics.GenericAPIView):
    queryset = User_Profile.objects.all()
    serializer_class = serializers.LogInSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user and user.is_staff: return self.is_token_valid(user=user)
        return Response({'error': _('Invalid Credentials')}, status=status.HTTP_400_BAD_REQUEST)


    def is_token_valid(self, user):
        try: token = Token.objects.get(user=user)
        except: token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)