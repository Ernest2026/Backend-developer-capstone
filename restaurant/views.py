from django.shortcuts import render
from rest_framework import generics
from .models import MenuItem
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Create your views here.
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer