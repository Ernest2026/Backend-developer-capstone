from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking
from rest_framework import serializers
from django.contrib.auth.models import User

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        # fields = '__all__'
        fields = ['title', 'price', 'inventory']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']