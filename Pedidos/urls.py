from django.urls import path
from Pedidos.views import inicio,cliente,empleado,pedido

urlpatterns = [
    path('inicio/', inicio),
    path('clientes/', cliente),
    path('empleados/', empleado),
    path('pedidos/', pedido),
]