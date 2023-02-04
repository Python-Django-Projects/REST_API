from rest_framework import serializers
from .models import User, Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['user', 'name', 'image']
