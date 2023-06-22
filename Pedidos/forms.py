from django import forms

class form_setClientes(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    telefono= forms.CharField(max_length=15)
    email= forms.EmailField()
    referencia= forms.CharField(max_length=30)

