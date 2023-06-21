from django.urls import path
from Pedidos.views import inicio,cliente,empleado,pedido, producto

urlpatterns = [
    path('inicio/', inicio, name='Inicio'),
    path('clientes/', cliente, name='Clientes'),
    path('empleados/', empleado, name='Empleados'),
    path('pedidos/', pedido, name='Pedidos'),
    path('productos/', producto, name='Productos'),
]