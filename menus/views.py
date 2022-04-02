from django.shortcuts import redirect, render
from django.http import HttpResponse

from menus.models import MenuItem, Restaurant

# Create your views here.


def show_menu(request, restaurant_id):
    """show a menu by restaurant"""
    menu_itens = MenuItem.objects.order_by('category')
    context = {'menu_itens': menu_itens}
    return render(request, "menus/show_menu.html", context)


def new_menu_item(request, restaurant_id):
    """create a new menu item for restaurante"""
    if request.method == 'POST':
        form_data = request.POST
        menu_item = MenuItem()
        menu_item.category = form_data.get('category')
        menu_item.name = form_data.get('name')
        menu_item.description = form_data.get('description')
        menu_item.price = form_data.get('price')
        menu_item.restaurant_id = restaurant_id
        menu_item.save()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, 'menus/new_menu_item.html', {'restaurant_id': restaurant_id})


def edit_menu_item(request, restaurant_id, item_id):
    """edit a menu item by a id."""
    menu_item = MenuItem.objects.get(pk=item_id)
    if request.method == 'POST':
        form_data = request.POST
        menu_item.category = form_data.get('category')
        menu_item.name = form_data.get('name')
        menu_item.description = form_data.get('description')
        menu_item.price = form_data.get('price')
        menu_item.save()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, 'menus/edit_menu_item.html', {'menu_item': menu_item})


def delete_menu_item(request, restaurant_id, item_id):
    menu_item = MenuItem.objects.get(pk=item_id)
    if request.method == 'POST':
        menu_item.delete()
        return redirect(f"/menus/{restaurant_id}")
    else:
        return render(request, 'menus/delete_menu_item.html', {'menu_item': menu_item})
