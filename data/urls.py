
from django.urls import path

from .views import *

app_name = 'data'
urlpatterns = [
    path('items/',items_list,name='items_list_url'),
    path('demand/',demand_list,name='demand_list_url'),

    path('item/create/',ItemCreate,name='item_create_url'),

    path('delete_items/<str:pk>/', delete_items, name="delete_items"),
    path('update_item/<str:pk>/',update_items,name="update_item"),
    path('issue_item/<str:pk>/',issue_items,name="issue_item"),
    path('add_inventory/<str:pk>/',add_inventory,name="add_inventory"),

# path('view/',view,name="view"),




    


]
