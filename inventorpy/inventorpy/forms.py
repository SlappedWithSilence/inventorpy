# inventory/forms.py
from django import forms
from .models import InventoryItem, InventoryTransaction, Project


class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'description', 'sku', 'project']


class InventoryTransacitonForm(forms.ModelForm):
    class Meta:
        model = InventoryTransaction
        fields = ['item', 'project', 'quantity', 'purchaser']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']
