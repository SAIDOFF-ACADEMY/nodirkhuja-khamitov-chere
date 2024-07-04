from user import serializers
from user.models import UserContactApplication


from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _



class LogInView(generics.GenericAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = serializers.LogInSerializer

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user and user.is_staff: return self.get_token(user)
        return Response({'error': _('Invalid Credentials')}, status=status.HTTP_400_BAD_REQUEST)


    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class UserEmailView(generics.GenericAPIView):

    def get(self, request):
        user = self.request.user
        if user:
            return Response({"email": user.email})
        return Response({"message":_("User does not exist")})

    
class UserContactApplicationListView(generics.ListAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = serializers.UserContacApplicationSerializer
    permission_classes = [permissions.IsAdminUser]


class UserContactApplicationEditView(generics.UpdateAPIView):
    queryset = UserContactApplication.objects.all()
    serializer_class = serializers.UserContacApplicationSerializer
    permission_classes = [permissions.IsAdminUser]
 

 