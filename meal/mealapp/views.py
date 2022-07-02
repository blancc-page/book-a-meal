from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView

# Create your views here.

class UsersView(APIView):
    
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

class CustomerView(APIView):
    def get(self, request, format=None):
        customers = CustomUser.objects.filter(is_customer=True)
        serializerdata = CustomUserSerializer(customers, many=True)
        return Response(serializerdata.data)

    def post(self, request, format=None):
        serializerdata = CustomUserSerializer(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
        return Response(serializerdata.errors)

class CatererView(APIView):
    def get(self, request, format=None):
        caterers = CustomUser.objects.filter(is_caterer=True)
        serializerdata = CustomUserSerializer(caterers, many=True)
        return Response(serializerdata.data)

    def post(self, request, format=None):
        serializerdata = CustomUserSerializer(data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
        return Response(serializerdata.errors)