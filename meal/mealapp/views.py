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

class CustomerDetailView(APIView):
    def get(self, request, pk, format=None):
        customer = CustomUser.objects.get(pk=pk)
        serializerdata = CustomUserSerializer(customer)
        return Response(serializerdata.data)

    def put(self, request, pk, format=None):
        customer = CustomUser.objects.get(pk=pk)
        serializerdata = CustomUserSerializer(customer, data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
        return Response(serializerdata.errors)

    def delete(self, request, pk, format=None):
        customer = CustomUser.objects.get(pk=pk)
        customer.delete()
        return Response(status=None)

class CatererDetailView(APIView):
    def get(self, request, pk, format=None):
        caterer = CustomUser.objects.get(pk=pk)
        serializerdata = CustomUserSerializer(caterer)
        return Response(serializerdata.data)

    def put(self, request, pk, format=None):
        caterer = CustomUser.objects.get(pk=pk)
        serializerdata = CustomUserSerializer(caterer, data=request.data)
        if serializerdata.is_valid():
            serializerdata.save()
            return Response(serializerdata.data)
        return Response(serializerdata.errors)

    def delete(self, request, pk, format=None):
        caterer = CustomUser.objects.get(pk=pk)
        caterer.delete()
        return Response(status=None)