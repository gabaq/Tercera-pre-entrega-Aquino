from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def inicio(request):
    return render(request,'Pedidos/inicio.html')

def cliente(request):
    return render(request,'Pedidos/clientes.html')

def empleado(request):
    return render(request,'Pedidos/empleados.html')

def pedido(request):
    return render(request,'Pedidos/pedidos.html')

def producto(request):
    return render(request,'Pedidos/productos.html')