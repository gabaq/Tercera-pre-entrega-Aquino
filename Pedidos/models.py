from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono= models.CharField(max_length=15)
    email= models.EmailField()
    referencia= models.CharField(max_length=30)
    
class Empleado(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    cargo= models.CharField(max_length=30)

class Pedido(models.Model):
    descripcion= models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado= models.BooleanField()