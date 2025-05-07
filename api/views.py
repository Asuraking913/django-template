from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

# Create your views here.

class RegisterUserView(generics.CreateAPIView):
	serializer_class = RegisterUserSerializer
	permission_classes = [AllowAny]


