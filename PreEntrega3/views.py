from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo (request):
    return HttpResponse("HW!")

def segunda_vista (self, nombre):
    data = f"Usuario: <h4> {nombre} </h4>"
    return HttpResponse (data)

def template_test(self):
    template1html = open ("./PreEntrega3/templates/template1.html")
    template1 = Template(template1html.read())
    template1html.close()
    context1 = Context()
    document1 = template1.render(context1)

    return HttpResponse(document1)

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
    document = template.render

    return HttpResponse(document)
