from django.urls import path
from Pedidos.views import *
#inicio,cliente,empleado,pedido, producto, setClientes,getClientes, buscarClientes
#from Pedidos import views
# views.inicio,
# views.cliente,
# etc

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('inicio/', inicio, name='Inicio'),
    path('clientes/', cliente, name='Clientes'),
    path('empleados/', empleado, name='Empleados'),
    path('pedidos/', pedido, name='Pedidos'),
    path('productos/', producto, name='Productos'),

    path('setClientes/', setClientes, name='setClientes'),
    path('getClientes/', getClientes, name='getClientes'),
    path('buscarClientes/', buscarClientes, name='buscarClientes'),

    path('setEmpleados/', setEmpleados, name='setEmpleados'),
    path('getEmpleados/', getEmpleados, name='getEmpleados'),
    path('buscarEmpleados/', buscarEmpleados, name='buscarEmpleados'),
]