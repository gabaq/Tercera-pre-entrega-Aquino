from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from Pedidos.models import *
from Pedidos.forms import *

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


def setClientes_old(request):
    if request.method == 'POST':
        cliente = Cliente  (nombre=request.POST["nombre"]
                            ,apellido=request.POST["apellido"]
                            ,telefono=request.POST["telefono"]
                            ,email=request.POST["email"]
                            ,referencia=request.POST["referencia"])
        cliente.save()
        return render(request,'Pedidos/inicio.html')
    return render(request, "Pedidos/setClientes.html")


# seccion Clientes

def setClientes(request):
    if request.method == 'POST':
        miFormulario = form_setClientes(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            cliente = Cliente  (nombre=data["nombre"]
                                ,apellido=data["apellido"]
                                ,telefono=data["telefono"]
                                ,email=data["email"]
                                ,referencia=data["referencia"])
            cliente.save()
            return render(request,'Pedidos/inicio.html')
    else:
        miFormulario = form_setClientes()
        return render(request, "Pedidos/setClientes.html", {"miFormulario":miFormulario})
setClientes

def getClientes(request):
    return render(request,'Pedidos/getClientes.html')


def buscarClientes(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Cliente.objects.filter(nombre = nombre)
        return render(request, 'Pedidos/getClientes.html', {"clientes":clientes})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)


# seccion Empleados

def setEmpleados(request):
    if request.method == 'POST':
        miFormulario = form_setEmpleados(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            data = miFormulario.cleaned_data
            empleado = Empleado  (nombre=data["nombre"]
                                ,apellido=data["apellido"]
                                ,email=data["email"]
                                ,cargo= data["cargo"])
            empleado.save()
            return render(request,'Pedidos/inicio.html')
    else:
        miFormulario = form_setEmpleados()
        return render(request, "Pedidos/setEmpleados.html", {"miFormulario":miFormulario})


def getEmpleados(request):
    return render(request,'Pedidos/getEmpleados.html')


def buscarEmpleados(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        empleados = Empleado.objects.filter(nombre = nombre)
        return render(request, 'Pedidos/getEmpleados.html', {"empleados":empleados})
    else:
        respuesta = "No se enviaron datos"
    return HttpResponse(respuesta)