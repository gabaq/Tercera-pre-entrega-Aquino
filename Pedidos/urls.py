from django.urls import path
from django.contrib.auth.views import LogoutView
from Pedidos.views import *
#inicio,cliente,empleado,pedido, producto, setClientes,getClientes, buscarClientes
#from Pedidos import views
# views.inicio,
# views.cliente,
# etc

urlpatterns = [
    path('', loginWeb, name='Login'),
    path('inicio/', inicio, name='Inicio'),

    path('login/', loginWeb, name='login'),
    path('register/', registerWeb, name='register'),
    path('logout/', LogoutView.as_view(template_name='Pedidos/login.html'), name='Logout'),

    path('productos/', producto, name='Productos'),

    path('clientes/', cliente, name='Clientes'),
    path('setClientes/', setClientes, name='setClientes'),
    path('getClientes/', getClientes, name='getClientes'),
    path('buscarClientes/', buscarClientes, name='buscarClientes'),

    path('empleados/', empleado, name='Empleados'),
    path('setEmpleados/', setEmpleados, name='setEmpleados'),
    path('getEmpleados/', getEmpleados, name='getEmpleados'),
    path('buscarEmpleados/', buscarEmpleados, name='buscarEmpleados'),

    path('pedidos/', pedido, name='Pedidos'),
    path('setPedidos/', setPedidos, name='setPedidos'),
    path('getPedidos/', getPedidos, name='getPedidos'),
    path('buscarPedidos/', buscarPedidos, name='buscarPedidos'),
]