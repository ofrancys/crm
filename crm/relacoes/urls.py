from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('clientes',views.index,name="clientes"),
    path('add_clientes',views.add_clientes,name="add_clientes"),
    path('edit_clientes/<int:id>',views.edit_clientes,name="edit_clientes"),
    path('delete_clientes/<int:id>',views.delete_clientes,name="delete_clientes"),
    path('pedidos',views.index,name="pedidos"),
    path('add_pedidos',views.add_pedidos,name="add_pedidos")
]