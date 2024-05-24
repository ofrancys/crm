from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),

    path('clientes',views.clientes,name="clientes"),
    path('add_clientes',views.add_clientes,name="add_clientes"),
    path('edit_clientes/<int:id>',views.edit_clientes,name="edit_clientes"),
    path('delete_clientes/<int:id>',views.delete_clientes,name="delete_clientes"),
    #path('pedidos',views.index,name="pedidos"),
    path('pedidos',views.pedidos,name="pedidos"),
    path('add_pedidos',views.add_pedidos,name="add_pedidos"),
    path('produtos',views.produtos,name="produtos"),
    path('add_produtos',views.add_produtos,name="add_produtos"),
    path('representadas',views.representadas,name="representadas"),
    path('add_representadas',views.add_representadas,name="add_representadas"),
]