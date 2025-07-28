from django.shortcuts import render
from django.urls import reverse
from rest_framework import viewsets
import requests

from inventory.models import Inventory, Supplier
from inventory.serializers import InventorySerializer, SupplierSerializer

# Create your views here.


class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    # queryset = Inventory.objects.all()

    def get_queryset(self):
        queryset = Inventory.objects.select_related("supplier").all()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()


def index(request):
    print(reverse("inventory"))
    return render(request, "index.html")


def inventory_details(request, id):
    item = Inventory.objects.get(id=id)
    return render(request, "inventory_details.html", {"item": item})
