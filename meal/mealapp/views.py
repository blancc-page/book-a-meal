from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here.
class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'user_id': user.pk,
            'email': user.email
        })


class CustomerView(APIView):
    
    def get(self, request, format=None):

        customers = CustomUser.objects.all()

        serializerdata = CustomUserSerializer(customers, many=True)

        return Response(serializerdata.data)
    
    def post(self, request, format=None):
        serializerdata = CustomUserSerializer(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
        return Response(serializerdata.errors)

class MenuView(generics.ListCreateAPIView):

    serializer_class = MenuSerializer

    queryset = Menu.objects.all()

