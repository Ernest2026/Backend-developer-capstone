# tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test data
        self.item1 = MenuItem.objects.create(title="Burger", price=50.00, inventory=20)
        self.item2 = MenuItem.objects.create(title="Pizza", price=100.00, inventory=15)
        self.client = APIClient()

    def test_getall(self):
        # Serialize the data
        menu_items = MenuItem.objects.filter(title="Burger")
        serializer = MenuItemSerializer(menu_items, many=True)
        
        # Assert the response data matches the serialized data
        self.assertEqual({"title": "Burger", "price": "50.00", "inventory": 20}, serializer.data[0])
