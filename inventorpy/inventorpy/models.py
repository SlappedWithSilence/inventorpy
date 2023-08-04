import django
from django.db import models


class InventoryItem(models.Model):
    """
    A basic inventory item.
    """
    sku = models.CharField(max_length=100)  # Unique internal inventory identifier
    name = models.CharField(max_length=100)  # User-facing name
    description = models.TextField()  # User-facing desc
    project = models.ForeignKey("Project", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.sku}"


class InventoryTransaction(models.Model):
    """
    A DB entry representing a change in the quantity of a specific unit of inventory
    """
    item = models.OneToOneField(
        InventoryItem,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.TimeField(default=django.utils.timezone.now())
    purchaser = models.CharField(max_length=100)

    @property
    def sku(self) -> str:
        return self.item.sku

    def __str__(self):
        return f"{str(self.item)} {'+' if self.quantity > -1 else ''}{self.quantity}"


class Project(models.Model):
    """
    A project is a collection of InventoryItems and InventoryTransactions.
    """

    id = models.fields.PositiveIntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"
