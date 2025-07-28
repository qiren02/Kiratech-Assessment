from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Inventory, Supplier


# For testing HTML views
class InventoryPageTests(TestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="Test Supplier")
        self.inventory = Inventory.objects.create(
            name="Test Item",
            description="second item",
            note="",
            stock="0",
            availability=True,
            supplier=self.supplier,
        )

    def test_inventory_list_page_returns_200(self):
        response = self.client.get(reverse("inventory"))  # url name for /inventory
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_page_returns_200(self):
        response = self.client.get(
            reverse("inventory_details_page", args=[self.inventory.id])
        )
        self.assertEqual(response.status_code, 200)


# For testing DRF API endpoints
class InventoryAPITests(APITestCase):
    def setUp(self):
        self.supplier = Supplier.objects.create(name="API Supplier")
        self.inventory = Inventory.objects.create(
            name="API Item",
            description="second item",
            note="",
            stock="0",
            availability=True,
            supplier=self.supplier
        )

    def test_inventory_api_returns_200(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_inventory_api_detail_returns_200(self):
        response = self.client.get(f'/api/inventory/{self.inventory.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
