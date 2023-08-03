from django.shortcuts import render, redirect
from .models import InventoryItem, Project
from .forms import InventoryItemForm, ProjectForm


def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/list_items.html', {'items': items})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'inventory/list_projects.html', {'projects': projects})


def add_inventory_item(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_item.html', {'form': form})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = InventoryItemForm()
    return render(request, 'inventory/add_project.html', {'form': form})
