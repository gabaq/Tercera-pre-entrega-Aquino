from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo (request):
    return HttpResponse("Welcome!")

def segunda_vista (self, nombre):
    data = f"Usuario: <h4> {nombre} </h4>"
    return HttpResponse (data)

def template_test(request):
    #template1html = open ("./PreEntrega3/templates/template1.html")
    #template1 = Template(template1html.read())
    #template1html.close()
    #context1 = Context()
    #document1 = template1.render(context1)
    #return HttpResponse(document1)
    return render(request,"template1.html")

def template_test2(self):
    nombre = "Gabriel"
    apellido = "Aquino"
    namelist = ["Gabriel", "Roman", "Coco", "German"]
    dictionary = {
        "nombre": nombre,
        "apellido": apellido,
        "namelist": namelist
    }
    template = loader.get_template("template1.html")
    document = template.render(dictionary)
    return HttpResponse(document)
