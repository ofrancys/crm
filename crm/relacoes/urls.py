from django.urls import path
from . import views 

urlpatterns = [
    path('',views.index),

    path('clientes',views.clientes,name="clientes"),
    path('add_clientes',views.add_clientes,name="add_clientes"),
    path('edit_clientes/<int:id>',views.edit_clientes,name="edit_clientes"),
    path('delete_clientes/<int:id>',views.delete_clientes,name="delete_clientes"),

    path('pedidos',views.pedidos,name="pedidos"),
    path('add_pedidos',views.add_pedidos,name="add_pedidos"),
    path('edit_pedidos/<int:id>',views.edit_pedidos,name="edit_pedidos"),
    path('delete_pedidos/<int:id>',views.delete_pedidos,name="delete_pedidos"),

    path('produtos',views.produtos,name="produtos"),
    path('add_produtos',views.add_produtos,name="add_produtos"),
    path('edit_produtos/<int:id>',views.edit_produtos,name="edit_produtos"),
    path('delete_produtos/<int:id>',views.delete_produtos,name="delete_produtos"),

    path('representadas',views.representadas,name="representadas"),
    path('add_representadas',views.add_representadas,name="add_representadas"),

    path('representantes',views.representantes,name="representantes"),
    path('add_representantes',views.add_representantes,name="add_representantes"),
]