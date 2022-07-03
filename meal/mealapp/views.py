from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

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
