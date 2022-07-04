from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class IndexView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'wsmg': "Welcome to Book-a-meal"
        }
        return Response(content)