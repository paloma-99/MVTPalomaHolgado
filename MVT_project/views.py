from django.http import HttpResponse
from django.template import Context, Template, loader
from datetime import date, datetime
import random

from MVT_app.models import Familiar

#def crear_familiar(request, nombre, apellido, edad):
#   familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad, fecha_nacimiento=datetime.now())
#    familiar.save()

#    template = loader.get_template('crear_familiar.html')
#    template_renderizado = template.render({'familiar':familiar})
#    return HttpResponse(template_renderizado)

def crear_familiar(request):
    familiar1 = Familiar(nombre='Lydia', apellido='Beuck', edad=85, fecha_nacimiento=datetime.now())
    familiar2 = Familiar(nombre='Bettina', apellido='Pretell', edad=56, fecha_nacimiento=datetime.now())
    familiar3 = Familiar(nombre='Manuel', apellido='Holgado', edad=22, fecha_nacimiento=datetime.now())
    familiar1.save()
    familiar2.save()
    familiar3.save()

    template = loader.get_template('crear_familiar.html')
    template_renderizado = template.render({})
    return HttpResponse(template_renderizado)


def ver_familiares(request):
    familiares = Familiar.objects.all()

    template = loader.get_template('ver_familiares.html')
    template_renderizado = template.render({'familiares':familiares})
    return HttpResponse(template_renderizado)
