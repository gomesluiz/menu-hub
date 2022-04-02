from django.urls import path
from . import views

urlpatterns = [
    path('<int:restaurant_id>', views.show_menu, name="menu"), 
    path('<int:restaurant_id>/new/', views.new_menu_item, name="new"),
    path('<int:restaurant_id>/edit/<int:item_id>/', views.edit_menu_item, name="edit"),
    path('<int:restaurant_id>/delete/<int:item_id>/', views.delete_menu_item, name="delete"),
]