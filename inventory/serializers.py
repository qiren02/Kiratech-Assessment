from rest_framework import serializers
from .models import *


class InventorySerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)

    class Meta:
        model = Inventory
        # fields = [
        #     "id",
        #     "name",
        #     "description",
        #     "note",
        #     "stock",
        #     "availability",
        #     "supplier",
        #     "supplier_name",
        # ]
        fields = "__all__"
        extra_kwargs = {
            'supplier': {'write_only': True}
        }


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
