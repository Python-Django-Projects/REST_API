from .models import Image
from .serializers import ImageSerializer
from rest_framework import generics
from rest_framework import mixins

# Create your views here.


class ImageList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
