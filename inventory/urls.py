from django.urls import include, path
from rest_framework import routers

from inventory import views
from inventory.views import InventoryViewSet, SupplierViewSet

router = routers.DefaultRouter()
router.register(r"inventory", InventoryViewSet, basename="inventory")
router.register(r"suppliers", SupplierViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("inventory/", views.index, name="inventory"),
    path("inventory/<int:id>/", views.inventory_details, name="inventory_details_page"),
]
