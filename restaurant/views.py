from django.shortcuts import render
from rest_framework import generics
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from rest_framework import serializers
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
