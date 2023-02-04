from django.shortcuts import render
from .models import *
from .serializers import UserSerializer, ImageSerializer
from rest_framework import generics

# Create your views here.


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
