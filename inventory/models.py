from django.db import models

# Create your models here.

class Supplier (models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)
    
class Inventory (models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=False)
    note = models.TextField(blank=True, null=False)
    stock = models.IntegerField()
    availability = models.BooleanField(default=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
    
